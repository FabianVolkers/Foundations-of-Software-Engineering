Your task is create a really simple version of Eliza, one of the first examples of a piece of software attempting artificial intelligence. Eliza is a real chatbot, implemented in 1966 - and its creation sparked many of the conversations we are still having today. For more on Eliza, there's a great podcast episode here https://99percentinvisible.org/episode/the-eliza-effect/ . There are also several fully interactive versions of Eliza online, for instance, here. http://www.med-ai.com/models/eliza.html

Let's do a simple version of the chatbot, which should run in the python console.

First, Eliza should introduce itself and ask you a question. Please aim for a total of about 3 interactions between the user and Eliza. You can run wild with this, here are some suggestions.
First, start with Eliza introducing itself and asking for user input. remember to use the Python "input" function: https://www.w3schools.com/python/ref_func_input.asp

The conversation can start like this:

Bot: "Hi, I am Eliza. What is your name?".
you input your name, e.g. Jenny. Then Eliza responds, addressing you by name:
Bot: "Hi Jenny, how what is on your mind today". Again, prompt the user for input.

At this point, the actual implementation of Eliza gets a bit complicated. Let's keep it simple and ignore full natural language processing. There are a few classic responses that are vague and open ended like "Tell me more", or "I see", or "I am not sure I understand, what exactly do you mean?". Have Eliza respond with a phrase like this, and ask for input again.

Ok, what's the point of this? Well, there is a lot hiding in this exercise:
- you are actively recalling some simple Python and the command line interface
- you are learning more features of glitch, like the console
- you are practicing interleaving, working on several skills at once. We will do this a lot in Foundations, switching contexts, methods, and tools.
- you are learning a bit about chatbots, human-computer interaction, and AI.