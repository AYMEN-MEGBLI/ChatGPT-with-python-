import openai
import time
# Define OpenAI API key (https://beta.openai.com/account/api-keys)
openai.api_key = "your api key"
# Set up the model and prompt
model_engine = "text-davinci-003"
while 1 :
    prompt =str(input("your question\t:"))
    start = time.time()
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
    end = time.time()
    print("The time used to execute this is given below  [",end - start,']')
    valid=False
    while not valid:
        condition=str(input('press [A] for another question | [S] saving response in external file | [L] Leaving  :   ')).upper()
        valid=condition in ['A','S','L']
    if condition=='S' :
        with open (prompt+".txt",'w') as f:
            f.write("-----------chatgpt-----------\n-question  :"+prompt+"\n-reponse  :"+reponse+"\n[BY Megbli Aymen]")
        print("file is maked")
        valid = False
        while not valid:
            condition = str(input('press [A] for another question | [L] Leaving  :   ')).upper()
            valid = condition in ['A','L']
    if condition=="L" :
        break

for i in range(5,-1,-1) :
    print('\r',i,end="")
    time.sleep(1)
quit()
