import gym
import time
env = gym.make('Breakout-v0')
env.reset()
for episode in range(100):
    observation = env.reset()
    for t in range(1000):
        env.render()
        print(observation)
        action  = env.action_space.sample()
        observation, reward, done,info = env.step(action)
        print(observation.shape)
        print(reward)
        print(info)
        env.step(env.action_space.sample())
        if done:
            print("Episode finished after {} timesteps".format(t+1))