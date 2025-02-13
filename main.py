# main.py
# from agent import generate_final_response

# if __name__ == "__main__":
#     print("Welcome to WeatherGenie CLI - Your Personalized Weather Advisor!")
#     user_query = input("Ask WeatherGenie a question: ")
#     response = generate_final_response(user_query)
#     print("\n" + response)

# main.py
from agent import generate_final_response

if __name__ == "__main__":
    print("Welcome to WeatherGenie CLI - Your Personalized Weather Advisor!")
    print("Type 'exit' to quit the application.")
    
    while True:
        user_query = input("Ask WeatherGenie a question: ")
        if user_query.strip().lower() == "exit":
            print("Goodbye!")
            break
        response = generate_final_response(user_query)
        print("\n" + response + "\n")
