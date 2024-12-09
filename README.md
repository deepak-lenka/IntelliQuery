# Assignment Part 2: 

# IntelliQuery

IntelliQuery is an intelligent agent built to fulfill the requirements of the following assignment:



1. Build an Agent that can perform smart actions based on the user's query.
2. Extend the service and host another endpoint for the agent.
3. The agent should reliably decide when to call the VectorDB and when not to. (e.g., "Hello" should not call the VectorDB)
4. Introduce at least ONE more action/tool that the Agent can invoke based on the user's query.

## How IntelliQuery Meets the Requirements

1. **Smart Actions**: The agent processes queries and performs actions like answering questions, telling jokes, and sharing fun facts.
2. **Multiple Endpoints**: Two endpoints are implemented - `/query` and `/agent`.
3. **VectorDB Decision**: The agent uses a `should_use_vectordb()` function to decide when to use the VectorDB.
4. **Additional Actions**: Two bonus actions are implemented - joke telling and fun fact sharing.

## Code Structure

- `main.py`: Contains the FastAPI application, agent logic, and endpoint definitions.
- `data.py`: Stores the VectorDB data.
- `static/index.html`: Simple frontend for interacting with the agent.

## How It Works

1. The agent receives a query through either `/query` or `/agent` endpoint.
2. It processes the query using the `process_query()` function:
   - Greetings are responded to without using VectorDB.
   - Questions are answered using VectorDB if appropriate.
   - Joke requests trigger the joke generator.
   - Fun fact requests trigger the fun fact generator.
3. The appropriate response is returned to the user.

## How to Run

1. Ensure you have Python installed (3.7+).

2. Clone the repository:
   ```
   git clone https://github.com/deepak-lenka/IntelliQuery.git
   cd IntelliQuery
   ```

3. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install dependencies:
   ```
   pip install fastapi uvicorn
   ```

5. Run the application:
   ```
   python main.py
   ```

6. Open a web browser and go to `http://localhost:8000` to interact with the agent.

## Testing the Agent

To test different functionalities, try the following queries:

1. Greeting: "Hello"
   - Expected: A greeting response without using VectorDB.

2. Question: "What is the largest planet?"
   - Expected: An answer from the VectorDB.

3. Joke Request: "Tell me a joke"
   - Expected: A random joke.

4. Fun Fact Request: "Share a fun fact"
   - Expected: A random fun fact.

5. Invalid Query: "abcdefg"
   - Expected: A prompt asking for a valid query.

## Future Improvements

- Expand the VectorDB with more information.
- Implement more creative actions.
- Enhance the frontend for a better user experience.
- Add unit tests for each component.
