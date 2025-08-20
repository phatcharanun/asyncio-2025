import asyncio
import random
import matplotlib.pyplot as plt

# Number of agents in the swarm
N_AGENTS = 10
# Maximum number of steps each agent can take
N_STEPS = 200

# Random target location within a grid (-20 to 20)
TARGET = (random.randint(-20, 20), random.randint(-20, 20))

# Dictionary to store the path (trace) of each agent
traces = {i: [(0, 0)] for i in range(N_AGENTS)}
# Dictionary to record which agent found the target and at which step
found_by = {}

# Flag to indicate if the target has been found by any agent
target_found = False


async def explore(agent_id: int):
    """
    Each agent performs a random walk until it finds the target
    or until another agent finds it.
    """
    global target_found
    x, y = traces[agent_id][0]  # starting position
    for step in range(1, N_STEPS + 1):
        # If another agent has already found the target, stop moving
        if target_found:
            break

        # Random walk: move one step in one of four directions
        dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        x, y = x + dx, y + dy
        traces[agent_id].append((x, y))

        # If this agent finds the target
        if (x, y) == TARGET:
            traces[agent_id].append(TARGET) # บันทึกตำแหน่ง target
            found_by[agent_id] = step  # record the agent and step
            target_found = True        # set the global flag
            print(f"Agent {agent_id} found the target at step {step}")
            break

        # Simulate asynchronous delay
        await asyncio.sleep(0.01)


async def main():
    print(f"Random target location: {TARGET}")
    # Launch all agents as asynchronous tasks
    tasks = [asyncio.create_task(explore(i)) for i in range(N_AGENTS)]
    await asyncio.gather(*tasks)

    # Plot the path of each agent
    for agent_id, path in traces.items():
        xs, ys = zip(*path)
        plt.plot(xs, ys, marker='.', alpha=0.6, label=f"Agent {agent_id}")
    
    # Plot the target location
    plt.scatter(*TARGET, c='red', s=100, marker='X', label='Target')

    plt.title("Swarm Exploration (Stop All on Target Found)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Print which agent found the target 
    if found_by:
        print(f"Target found by:")
        for agent, step in found_by.items():
            print(f"Agent {agent} at step {step}")
    else:
        print("No agent found the target.")

if __name__ == "__main__":
    asyncio.run(main())