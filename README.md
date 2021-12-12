## 💡 Inspiration
- Due to the covid-19 pandemic, we all are forced to maintain social distancing to stop the spread of coronavirus. 
- We are visiting so many places like shopping malls, salons, hospitals, etc and there due to more rush we have to stand in long queues. So, this problem of lack of a proper crowd management system inspired us to develop Tokenizer which helps people to book appointments for the place which they want to visit in advance so that they don't have to stand in long queues. 

## ⚙ What it does
- The tokenizer is a platform where anyone can book appointments for crowded places where they have to stand in long queues. 
- User first has to register or log in to our platform then they have to choose a category for which they need to book an appointment. 
- Then appropriate places for that category will be shown. 
- To book an appointment user has to click on that place and then have to fill in booking details like booking date, time, and phone number (to send confirmation message). 
- After booking an appointment user will get a confirmation message on WhatsApp. 
- Users can also use voice assistant which we have built using Alan to perform operations like seeing bookings, getting a list of places according to his/her choice, etc. 

## How we built it
- To design a user interface or we can say frontend we have used HTML, CSS, and Javascript. We have used Flask (Python web framework) to communicate with firebase and Twilio API. 

#### Google Dev Library
- We have used Firebase for user authentication and Firestore to store data. 

#### Twilio 
- We have used Twilio's Whatsapp API to send confirmation messages to users (for this hackathon we are sending it to just one number). 

#### Alan SDK
- We have used Alan SDK to provide voice-based assistance on our website and perform basic operations based on voice commands.  

## 💪 Challenges we ran into
- We have faced issues in integrating firebase and structuring data properly in firestore but later on, we have solved it. 
- Another challenge for us is to use Sponsor tools like Alan and Twilio. Due to some limitations, we are not able to send confirmation messages from Twilio to every user. 

## 🙌 Accomplishments that we're proud of
We are happy that at last we are able to complete our project and almost integrate all the features that we are thought of. We have successfully deployed our application on the cloud and are able to integrate sponsor tools like Twilio API, Alan SDK, and Google Dev Library (Firebase).

## 📚 What we learned
- We learned how to use Twilio API to send messages on WhatsApp. 
- We have also learned how to create a voice-enabled assistant using Alan SDK. We learned how to deploy our application on the cloud. 

## 💭 What's next for Tokenizer - Never stand in long queues
- Improve user interface.
- Integrate more features like showing places according to user's location and proper dashboard for place owners. 
- Build mobile application. 
