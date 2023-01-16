import openai
from time import sleep,time
from colorama import init, Fore
from os import remove
init()
#initialize module colorama
# Define OpenAI API key (https://beta.openai.com/account/api-keys)
openai.api_key = "your API (https://beta.openai.com/account/api-keys) "
# Set up the model and prompt
model_engine = "text-davinci-003"
while 1 :
    prompt =str(input("your question\t:"))
    start = time()
    # Generate a response
    completion = openai.Completion.create\
        (
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        )

    reponse = completion.choices[0].text
    print('-'*100,reponse)
    end = time()
    print("The time used to execute this is given below  [",end - start,']')
    valid=False
    while not valid:
        condition=str(input('press ['+Fore.RED+'A'+Fore.WHITE+'] for another question | ['+Fore.RED+'S'+Fore.WHITE+'] saving response in external file | ['+Fore.RED+'L'+Fore.WHITE+'] Leaving  :   ')).upper()
        valid=condition in ['A','S','L']
    if condition=='S' :
        try :
            x="-----------chatgpt-----------\n-question  :"+prompt+"\n-reponse  :"+reponse+"\n[BY Megbli Aymen]"
            with open (prompt+".txt",'w') as f:
                    f.write(x)
            print(Fore.YELLOW,"file is created",Fore.WHITE)
        except UnicodeEncodeError:
            remove(prompt+".txt")
            print(Fore.RED, "error ! file not created", Fore.WHITE)
        valid = False
        while not valid:
            condition = str(input('press ['+Fore.RED+'A'+Fore.WHITE+'] for another question | ['+Fore.RED+'L'+Fore.WHITE+'] Leaving  :   ')).upper()
            valid = condition in ['A','L']
    if condition=="L" :
        break

for i in range(3,-1,-1) :
    print('\r',i,end="")
    sleep(1)
quit()
