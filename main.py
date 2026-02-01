import os
from dotenv import load_dotenv
import argparse
from prompts import system_prompt
from call_function import available_functions, call_function

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()



####

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key == None:
    raise RuntimeError("key not found")
####

from google import genai

client = genai.Client(api_key=api_key)
###

from google.genai import types






def main():
    prompt = args.user_prompt
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]



    '''
    if args.verbose:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")
    '''     






    for _ in range(20):
                
        responce = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt),
        )
        if responce.usage_metadata is None:
            raise RuntimeError("Gemini API response appears to be malformed")

            
        prompt_tokens = responce.usage_metadata.prompt_token_count
        response_tokens = responce.usage_metadata.candidates_token_count


        
        function_calls = responce.function_calls
        for candidate in responce.candidates:
            messages.append(candidate.content)

        if function_calls:
            function_results = []
            for function_call in function_calls:
                # call the helper with the FunctionCall object
                result = call_function(function_call, args.verbose)

                # 1. parts must exist
                if not result.parts:
                    raise RuntimeError("Function call returned no parts")

                first_part = result.parts[0]

                # 2. function_response must exist
                if not first_part.function_response:
                    raise RuntimeError("Missing function_response in part")

                # 3. response must exist
                if not first_part.function_response.response:
                    raise RuntimeError("Missing response in function_response")

                # 4. store the part
                function_results.append(first_part)

                # 5. in verbose mode, print the function result
                if args.verbose:
                    print(f"-> {first_part.function_response.response}")
            messages.append(types.Content(role="user", parts=function_results))


        else:
            print(responce.text)
            break

    else:
        print("Max iterations reached")




if __name__ == "__main__":
    main()
