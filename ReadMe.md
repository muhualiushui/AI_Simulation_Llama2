## Abstract

This project is an alternative to [Generative Agents](https://github.com/joonspk-research/generative_agents.git), substituting the GPT model with the Llama model from the University of Illinois at Urbana-Champaign. The aim is to conduct simulations with specific persona settings and evaluate the Llama model's performance in interactions resembling human-like NPC communication.

## Files Modified

- `reverie/backend_server/persona/prompt_template/gpt_structure.py`
- `reverie/backend_server/persona/prompt_template/run_gpt_prompt.py`

For the details of the changes, see the comments within the files.

**New File Added:**
- `reverie/backend_server/API.py` (Used for accessing the Llama model)

## Simulation Steps

### Step 1

Open a terminal and navigate to the frontend_server directory.

```bash
cd environment/frontend_server
```
Then run the server.
```bash
python manage.py runserver
```

### Step 2
In another terminal, navigate to the backend_server directory. 
```bash
cd reverie/backend_server
```
Then run the backend.
```bash
python reverie.py
```
### Step 3
Follow the on-screen instructions for setup.

1. You'll be prompted to "Enter the name of the forked simulation." Go to `environment/frontend_server/storage` to see package names:
  - `base_the_ville_isabella_maria_klaus` (Smaller simulation with 3 people)
  - `base_the_ville_n25` (Larger simulation with 25 people)
  For testing, use `base_the_ville_isabella_maria_klaus`.

2. You'll then be prompted to "Enter the name of the new simulation." Type a name, e.g., "test-simulation".

3. At the "Enter option:" prompt, type `run` followed by a number to specify the simulation duration, like `run 10` or `run 100`.

# Final Steps:
- To save the results, type "fin".
- To exit without saving, type "exit".
- To run another simulation, type "run" followed by a number.





