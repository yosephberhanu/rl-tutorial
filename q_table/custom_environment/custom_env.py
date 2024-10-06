import numpy as np
from PIL import Image # For visualization of our environment
import cv2 # For visualization of our environment
from matplotlib import style 
SIZE = 10                  # Size of Env
MOVE_PENALTY = 1           # Penalty for every move (To encourage finding the food fast)
ENEMY_PENALTY = 300        # Penalty for running into the enemy
FOOD_REWARD = 25           # Reward when our blob find the food
IMAGE_SIZE = 300
MAX_STEPS = 200            # Maximum number steps before player runs out of time


PLAYER = 1               # Player key in dict
FOOD = 2                 # Food key in dict
ENEMY = 3                # Enemy key in dict
COLORS = {
    PLAYER : (255, 175, 0),       # Blue
    FOOD: (0, 255, 0),            # Green
    ENEMY: (0, 0, 255)            # Red
}

style.use("ggplot")


class Blob:
    def __init__(self, color=(0,0,0)):
        self.x = np.random.randint(0, SIZE)
        self.y = np.random.randint(0, SIZE)
        self.color = color

    def __str__(self):
        return f'{self.x}, {self.y}'
    
    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y)
    
    def move(self, x = False, y = False):
        ''' 
        Move this blob
        '''

        # If no x, move randomly
        if not x:
            self.x += np.random.randint(-1, 2)
        # If no y, move randomly
        if not y:
            self.y += np.random.randint(-1, 2)
        self.x += x 
        self.y += y

        # Make sure we are not out of bounds
        if self.x < 0 :
            self.x = 0
        elif self.x > SIZE-1:
            self.x = SIZE-1

        if self.y < 0 :
            self.y = 0
        elif self.y > SIZE-1:
            self.y = SIZE-1
    
    def action(self, choice):
        '''
        Gives us 4 total movemtn options: {0,1,2,3}
        '''
        if choice == 0:
            self.move(x=1, y=1)
        elif choice == 1:
            self.move(x=-1, y=-1)
        elif choice == 2:
            self.move(x=-1, y=1)
        elif choice == 3:
            self.move(x=1, y=-1)

    # Override ==  to check for overlap
    def __eq__(self, other):
        if isinstance(other, Blob):
            return self.x == other.x and self.y == other.y
        return False
    
class BlobEnvironment:
    def __init__(self, env_mode=None, render_mode='none'):
        self.env_mode = env_mode
        self.render_mode = render_mode
        self.reset()
    
    def has_won(self):
        return self.player == self.food
    
    def has_lost(self):
        return self.player == self.enemy
    
    def is_alive(self):
        return self.alive
    
    def is_done(self):
        return self.has_won() or self.has_lost() or not self.is_alive()
    
    def reset(self):
        self.player = Blob(COLORS[PLAYER])
        self.enemy = Blob(COLORS[ENEMY])
        self.food = Blob(COLORS[FOOD])
        self.reward = 0
        self.no_steps = 0
        self.alive = True
        cv2.destroyAllWindows()
        return self.get_obs(), self.reward, self.has_won(), self.is_alive(), {}

    def step(self, action):
        if not self.is_alive():
            return self.get_obs(), self.reward, self.has_won(), self.is_alive(), {}
        self.no_steps += 1
        self.player.action(action)
        # Check if payer run into the enemy
        if self.has_lost():
            self.reward = -ENEMY_PENALTY
            self.alive = False
        # Check if payer run into the food
        elif self.has_won():
            self.reward = FOOD_REWARD
        else:
            self.reward = -MOVE_PENALTY
        if self.no_steps > MAX_STEPS:
            self.alive = False
        return self.get_obs(), self.reward, self.has_won(), self.is_alive(), {}
    
    def render(self, title = "Blobs"):
        env = np.zeros((SIZE, SIZE, 3), dtype=np.uint8)  # starts an rbg of our config.SIZE
        for b in [self.player, self.enemy, self.food]:
            env[b.x][b.y] = b.color
        img = Image.fromarray(env, 'RGB')  # reading to rgb. Apparently. Even tho color definitions are bgr. ???
        cv2.imshow(title, np.array(img.resize((IMAGE_SIZE, IMAGE_SIZE))))  # show it!
        
        if self.is_done():
            if cv2.waitKey(500) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
        else: 
            cv2.waitKey(50) & 0xFF == ord('q')
    def shutdown(self):
        cv2.destroyAllWindows()
        cv2.waitKey(1)  # Ensure all windows are closed before exiting

    def get_obs(self):
        if self.env_mode == 'cnn':
            env = np.zeros((SIZE, SIZE, 3), dtype=np.uint8) 
            for b in [self.player, self.enemy, self.food]:
                env[b.x][b.y] = b.color
            img = Image.fromarray(env, 'RGB')  # reading to rgb. Apparently. Even tho color definitions are bgr. ???
            return np.array(img.resize((IMAGE_SIZE, IMAGE_SIZE))) 
        else:
            return (self.player - self.food, self.player - self.enemy)