'''
This code is from tutorial -
https://medium.com/emergent-future/simple-reinforcement-learning-with-tensorflow-part-0-q-learning-with-tables-and-neural-networks-d195264329d0
'''
import gym
import numpy as np


#Load gym environment 
env = gym.make('FrozenLake-v0')

#Implement Q-Table learning algorithm
#Initialize table with all zeros
#observation_space is states = 16 and action_space is actions = 4
# Q is of size 16*4
Q = np.zeros([env.observation_space.n,env.action_space.n])
print('Q :: ', Q)

# Set learning parameters
lr = .85
y = .99  #discount factor
num_episodes = 2000

#create lists to contain total rewards and steps per episode - revisit??
#jList = []
rList = []

for i in range(num_episodes):
    # Reset environment and get first new observation
    s = env.reset()
    rAll = 0  #overall reward
    d = False
    j = 0   #exploration parameter - how many times you want to try values of Q

    # The Q-Table learning algorithm
    while j < 99:
        j += 1
        # Choose an action by greedily (with noise) picking from Q table
        a = np.argmax(Q[s, :] + np.random.randn(1, env.action_space.n) * (1. / (i + 1)))
        # Get new state and reward from environment
        s1, r, d, _ = env.step(a)
        # Update Q-Table with new knowledge
        Q[s, a] = Q[s, a] + lr * (r + y * np.max(Q[s1, :]) - Q[s, a])  #why adding in previous q-value - revisit
        rAll += r
        s = s1
        if d == True:
            break
    # jList.append(j)
    rList.append(rAll)

print "Score over time: " +  str(sum(rList)/num_episodes)
print "Final Q-Table Values"
print Q