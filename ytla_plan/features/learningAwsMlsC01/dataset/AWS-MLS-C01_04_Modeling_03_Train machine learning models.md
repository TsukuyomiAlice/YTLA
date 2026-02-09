### Train machine learning models

#### Reinforcement Learning
  * You have some sort of agent that "explores" some space
  * As it goes, it learns the value of different state changes in different conditions
  * Those values inform subsequent behavior of the agent as from learnings a model is created
  * Examples: Pac-Man, Cat & Mouse game (game Al)
    * Supply chain management
    * HVAC systems
    * Industrial robotics
    * Dialog systems
    * Autonomous vehicles
  * Yields fast on-line performance once the space has been explored

#### Q-Learning
  * A specific implementation of reinforcement learning
  * You have:
    * A set of environmental states s
    * A set of possible actions in those states a
    * A value of each state/action Q
  * Start off with Q values of 0
  * Explore the space
  * As bad things happen after a given state/action, reduce its Q
  * As rewards happen after a given state/action, increase its Q
  * What are some state/actions here?
    * Pac-man has a wall to the West
    * Pac-man dies if he moves one step South
    * Pac-man just continues to live if going North or East
  * You can "look ahead" more than one step by using a discount factor when computing Q (here s is previous state, s' is current state)
    * Q(s,a) += discount * (reward(s,a) + maxQ(s')) - Q(s,a))

#### Q-learning exploration
  * How do we efficiently explore all of the possible states?
    * Simple approach: always choose the action for a given state with the highest Q. If there's a tie, choose at random
      * But that's really inefficient, and you might miss a lot of paths that way
    * Better way: introduce an epsilon term
      * If a random number is less than epsilon, don't follow the highest Q, but choose at random
      * That way, exploration never totally stops
      * Choosing epsilon can be tricky
  * You can make an intelligent Pac-Man:
    * Have it semi-randomly explore different choices of movement (actions) given different conditions (states)
    * Keep track of the reward/penalty associated with each choice for a given state/action (Q) and can propagate rewards and penalties backwards multiple steps for better performance
    * Use those stored Q values to inform its future choices

##### Markov Decision Process
  * A mathematical framework/notation for modeling decision making (Q-learning) in situations where outcomes are partly random and partly under the control of a decision maker.
  * States are described as s and s'
  * State transition functions are described as Pa (s, s')
  * Our "O" values are described as a reward function Ra (s, s')
  * MDP is a discrete time stochastic control process.

#### Loss Functions (aka Cost Function): seek to calculate/minimize the error (difference between actual and predicted value)





