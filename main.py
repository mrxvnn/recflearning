import os 
from google import genai
from google.genai import types
import config

client = genai.Client(api_key ='AIzaSyBTM5aD8Ngvhg_j0YonkJACURE8Hdb3iWY')

def generate_response(prompt,temperature=0.3):
    try:
        contents = [types.Content(role='user',parts=[types.Part.from_text(text=prompt)])]
        config_params = types.GenerateContentConfig(temperature=temperature)
        response = client.models.generate_content(model='gemini-2.0-flash',contents=contents,config=config_params)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
    
def reinforcement_learning_acticity():
    print('\n===REINFORCEMENT LEARNING ACTICITY===\n') 

    prompt = input('Enter a prompt for the AI model :') 
    initial_response = generate_response(prompt)
    print(f"\n Initial AI Response: {initial_response}") 

    rating  = int(input('Rate the response from 1(bad) to 5(good) :'))
    feedback = input('Provide feedback for improvement :')

    improved_response  = f"{initial_response} (Improved with your feedback:{feedback})"
    print(f'\nImproved AI response:{improved_response}')

    print('\nReflection:')
    print('1. How did the response improve with feedback?') 
    print('2. How does reinforcement learning help AI to improve its performance over time?')

def role_based_prompt_activity():
    print('\n===ROLE BASED PROMPT ACTIVITY===\n')

    category = input('Enter a category (eg. science, maths):')
    item = input(f"Enter a specific {category} topic :")
    
    teacher_prompt = f"You are a techer,Explain {item} in simple terms."
    expert_prompt = f'You are an expert in {category}. Explain {item} in a detailed and technical manner.'

    teacher_response = generate_response(teacher_prompt)
    expert_response  = generate_response(expert_prompt)

    print(f"\n--- Teacher's Perspective ---\n{teacher_response}")
    print(f"\n--- Expert's Perspective ---\n{expert_response}")

    print('\nReflection')
    print('1.How did the AI response differ between the teacher and expert perspectives?')
    print('2. How can role based prompts help tailor AI responses for different contexts?')

def run_acticity():
    print('\n=== AI LEARNING ACTIVITY===\n')

    choice = input('Which activity would you like to run?(1:Reinforcement Learning, 2:Role Based Prompts):')
    if choice=='1':
        reinforcement_learning_acticity()
    elif choice=='2':
        role_based_prompt_activity()
    else:
        print('Invalid Choice! Choose 1 or 2.')

if __name__=="__main__":
    run_acticity()      




 
