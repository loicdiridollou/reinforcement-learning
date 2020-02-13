import gym
import numpy as np
import matplotlib.pyplot as plt

env = gym.make("CartPole-v1")
env.reset()

print(env.action_space)

'''
done = False
while not done:
    action = 1
    new_state, reward, done, _ = env.step(action)
    print(reward, new_state)
    env.r
'''
