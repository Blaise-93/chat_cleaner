# __Data Cleaning Made Easy__:

# __Introduction__

According to Wikipedia "Data analysis is the process of inspecting, cleansing, transforming, and modeling data with the goal of discovering useful information, informing conclusions, and supporting decision-making."  Data analysis is a great concept that we implement in machine learning and artificial intelligence. In machine learning procedural training of our model, we cannot achieve that without data, measurable factual information - this data can be exported to our program to help us with what we want to analyze, or the machine tool we want to build for example a chatbot.
We use data in our daily life activities even without noticing. 

For example, in our family, we can collect our favorite food our children or parents like via the usage of data analysis, which will help us with pre-informed decisions of likely food to prepare more often or during special occasions like Christmas, Ramadan, etc. This is made possible with the use of data analysis processes and statistical toolkits like mean, average, and median.  The same approach of data analysis can be employed, however in a complex format by a company or business organization to make great pre-informed decisions about their market trends, customers behavior, and how to better engage their customers as well as potential clients.

## Data Analysis Processes:
For a comprehensive data analysis, we employ a variety of essential processes:
- **Collecting Data**: We gather relevant data from diverse sources, including WhatsApp, Telegram, Facebook, Twitter, books, libraries, etc. Today, we’ll focus on using WhatsApp as our data source.

- **Cleaning Data**: Data cleaning ensures the quality and accuracy of our dataset. By addressing inconsistencies and anomalies, we ensure that the data accurately reflects the true values being measured. Python is our tool of choice for data cleaning, given its flexibility and powerful libraries like Pandas.

Other essential processes we employ for a comprehensive data analysis which is beyond the scope of this article, however, what mentioning include:
- **Transforming Data**: Preparing data for analysis (e.g., normalization, aggregation).

-  **Descriptive Analysis**: Summarizing and visualizing data.

- **Inferential Analysis**: Drawing conclusions based on sample data.

- **Predictive Analysis**: Forecasting future trends.

- **Prescriptive Analysis**: Recommending actions based on insights.

## __Why You Need This Project:__

Developers, kindly listen up! 🚀 If you're knee-deep in data analysis and crave a swift solution for tidying up your messy datasets, this project is your knight in shining code. Here's why it's a must-have:

1. **Effortless Setup**: Forget about wrestling with dependencies. With this project, all you need is your trusty Python installation. No fuss, no muss!

2. **Data Cleaning on Steroids**: Got hefty datasets that resemble a tangled spaghetti bowl? Fear not! Our module is battle-tested and ready to tackle even the gnarliest data messes. Cleanliness is next to data-godliness, after all.

3. **Machine Learning Magic**: If you're training models for ML or AI, consider this your secret weapon. It'll whip your data into shape faster than you can say "gradient descent."

4. **Plug-and-Play**: Import it seamlessly into your existing project. No arcane rituals required—just pure, unadulterated data-cleaning goodness.
5. **Unit Test Cases**: Concerned about function assertions? No need to worry! The majority of our functions have undergone thorough testing using the Unittest library. So, feel assured—your use cases are accounted for. You can check them [here](chats/test_cleaned_corpus.py).

So, fellow developer, grab this module, wield it like a digital broom, and sweep away those data cobwebs! 🧹💻


## Project SetUp : For those that would like to use their WhatsApp Chats 
Exporting and cleaning up data from WhatsApp can be intriguing, but it is very easy to accomplish if you follow the guidelines below. I will urge you to do the following export and clean up the data which we shall further explore in this article because I believe the best way to learn is by doing it yourself even if it means that you repeat the same concept several times, till you get it right. So, let's dive in, I hope you are as excited as I am. Are you ready?

1. Open your WhatsApp app, and select any of your friends, relatives, or a group you want by clicking on the person's chat menu as you normally do if you want to chat with someone on WhatsApp.

2. At the top right corner of the person's chat, you will see three-dotted (⁝) icons, click on it. A drop-down menu will appear, select More, and you will see Export chat. Click on the Export chat, and kindly select Without media in case it pops up. Kindly wait for the initialization process to finish.

3. Select the mode you would want WhatsApp to share your exported chat file, e.g. via an Email or through Drive.

4. So, once you are done, your file will have looked something similar to mine, as you can see in the link provided.  


## __Getting Started__:

Exporting and cleaning up data from WhatsApp can be intriguing, but it is very easy to accomplish if you follow the guidelines below. I will urge you to do the following export and clean up the data which we shall further explore in this article because I believe the best way to learn is by doing it yourself even if it means that you repeat the same concept several times, till you get it right. So, let's dive in, I hope you are as excited as I am. Are you ready?
- Open your WhatsApp app, and select any of your friends, relatives, or a group you want by clicking on the person's chat menu as you normally do if you want to chat with someone on WhatsApp.

-  At the top right corner of the person's chat, you will see three-dotted (⁝) icons, click on it. A drop-down menu will appear, select More, and you will see Export chat. Click on the Export chat, and kindly select Without media in case it pops up. Kindly wait for the initialization process to finish.

- Select the mode you would want WhatsApp to share your exported chat file, e.g. via an Email or through Drive.

- So, once you are done, your file will have looked something similar to mine, [WhatsApp Chat](https://drive.google.com/file/d/1qaBGtVF18zyRt5bKH3KQe4J1zm_ZWF4V/view?usp=drivesdk). You can download the chat corpus if you were not able to follow the steps above, for our data cleaning with Python, which we shall talk about later.

- Kindly make sure that you have Python installed on your computer, and any IDE of your choice will just work fine, if you don't have Python installed on your computer, download it [here](https://www.python.org/downloads/release/python-3121), and for the IDE, I use Visual Studio Code (VsCode), so please download it [here](https://code.visualstudio.com/download) as well. Follow all the installation processes as required for you to get everything right based on how we shall manipulate and clean our data later on. Once you are done with the installation, head over to the VSCode to create a project folder or file for the work through which we shall name cleaned_corpus.py. If you are a bit confused about how to get started with VsCode in Python as a beginner, then check out this tutorial, here.

__NB__: The WhatsApp chat data is already on this project at the *chats.txt* of the chats 
folder. So, all you need to do is to replace the file with your exported chat data from WhatsApp.

### A quickstart of cloning the repo:

To **clone a Git repository** using the command line in either **Windows (Command Prompt)** or **Linux**, follow these steps:

1. **Open your terminal** (either Command Prompt on Windows or Terminal on Linux).

2. **Navigate to the directory** where you want to create a local copy of the repository. You can use the `cd` command to change directories. For example:
    ```bash
    cd path/to/your/desired/directory
    ```

3. **Copy the URL** of the repository you want to clone. You can find this URL on the GitHub repository page under the "Code" button. Choose the HTTPS:
    - **HTTPS**: Click the HTTPS link and copy the URL, [Project HTTPS Link](https://github.com/Blaise-93/cleaned_chat.git)


4. **Run the `git clone` command** followed by the URL you copied above.
For example:
    ```bash
    git clone https://github.com/Blaise-93/cleaned_chat.git
    ```

5. Press **Enter** to create your local clone. You'll see output similar to this:
    ```
    Cloning into 'YOUR-REPOSITORY'...
    remote: Counting objects: 10, done.
    remote: Compressing objects: 100% (8/8), done.
    remote: Total 10 (delta 1), reused 10 (delta 1)
    Unpacking objects: 100% (10/10), done.
    ```

And that's it! You've successfully cloned the Git repository to your local machine. Now you can work on the project, make changes, 
and push them back to the remote repository on GitHub. Don't forget you can still download the Zip of the clone, extract and import it in your existing project as another option. 🚀


Certainly! Your paragraph provides clear instructions on how to use the settings in a Python project. However, to make it more engaging and appealing to developers, consider the following tweaks:

---

## **Fine-Tuning Your Settings: A Dev's Guide**

In your `settings.py` file of this project, you hold the keys to customization. Let's dive into how you can wield this power:

1. **The `UNWANTED_WORDS_OR_PHRASES` Constant:**
   - This gem allows you to filter out undesirables from your dataset.

   - Add any pesky words or phrases to the list. For instance, if you're tired of seeing those pesky full stops (.), just toss them in there.

   - Here's the magic incantation:
     ```python
     UNWANTED_WORDS_OR_PHRASES = [
         'pm', "am", ":", '\u200d♂', "px king cj",
         # Remove this line if you're not using my exported chat
         # Feel free to add more phrases, if any. :)
     ]
     ```
   - Now your data will be cleaner than a freshly linted codebase!

2. **Bonus Tip: Exported Chat Cleanup:**
   - If you're not using my exported chat, consider removing the mysterious `"px king cj"` line. It's like debugging a cryptic error message—sometimes you just need to let go.

Don't forget that you can actually allow your emojis to show up in your further data processing via commenting 
this line of code (`cleaned = re.sub(r'[\U00010000-\U0010ffff]', '', cleaned)`) as shown below code snippets.

```py
def clean_messages(messages):
    """ helps us remove emojis, media omitted times, names and times which 
        is attached when the log chats is generated from clean_corpus via 
        usage of regex methods.

        ::  returns a tuple.
     """
    
    cleaned_messages = []
    for message in messages:

        # Remove dates, media omitted, times, names, hyphens, and emojis
        cleaned = re.sub(r'<Media omitted>|\d{1,2}/\d{1,2}/\d{2,4}, \d{1,2}:\d{2}\u202f[APM]{2} - \w+: ', '', message)
        
        # comment the below line of code if you want to make use of emojis of all types
        # once it is commented with "#" it will definitely allow emojis visibility.
        #ALLOW_EMOJI
       
        cleaned = re.sub(r'-', '', cleaned)
        cleaned = re.sub(r'[\U00010000-\U0010ffff]', '', cleaned)
        cleaned_messages.append(cleaned)
    return tuple(cleaned_messages)


```

Remember, settings are like code comments: they're often overlooked but can save you from a world of chaos. Happy tweaking! 🚀



## How your data will look like on CMD prompt
Your data which you had printed on command line via using print statement will look like [this](images/cleaned_corpus.png) when you are done. 

## Acknowledgment:
- [Wikipedia](https://en.wikipedia.org/wiki/Data_analysis)
- [Data analysis | Definition, Research, & Methodology | Britannica](https://www.britannica.com/science/data-analysis)
- [Real Python Community](https://realpython.com/build-a-chatbot-python-chatterbot/)
- Special shout out to Python Developers' Community


## For Contribution:

If you find this project useful for your work and see areas where improvements can be made, we encourage you to:

__Make Pull Requests__: Contribute directly by submitting code changes or enhancements.

__Raise Issues__: If you encounter any problems or have suggestions, don’t hesitate to open an issue.

__Contact Me__: Feel free to reach out if you have questions or need guidance. You can reach me via the links I provided below.

Let’s collaborate to make this project even better!

Kindly share my work, and follow me on [Linkedin](https://www.linkedin.com/in/ejikeme-blaise-2504111b1/), [Twitter](https://twitter.com/Blaisemat6/)
and [GitHub](https://github.com/Blaise-93) for more educative content.
You can text me as well via my <ejikemeblaise08@gmail>


Thank you for reading.

