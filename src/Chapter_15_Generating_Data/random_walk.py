from random import choice
import matplotlib.pyplot as plt  # type: ignore

class RandomWalk:
    """A class to generate random walks."""
    
    def __init__(self, num_points=5000):
        """Initialize the attributes of the walk."""
        self.num_points = num_points
        
        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        """Calculate all the points in the walk."""
        
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            
            # Decide which direction to go, and how far to go.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            
            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue
            
            # Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            self.x_values.append(x)
            self.y_values.append(y)
            
# make a random walk
rw = RandomWalk(num_points=5000)
rw.fill_walk()

# plot the points in the walk
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
ax.set_aspect('equal')
plt.show()
