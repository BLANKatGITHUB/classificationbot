
# Dog-Cat Classification Bot 🐶🐱

Uses machine learning to classify whether image is cat or dog.

## Features
- **Image Classification**: Upload an image, and the bot will classify it as a "dog" or a "cat" using a TensorFlow CNN model.
- **Slash Commands**:
  - `/dog_or_cat`: Classify an uploaded image.
  - `/hello`: Receive a friendly greeting from the bot.
- **Error Handling**: Validates file types and gracefully handles processing errors.
- **Cloud Deployment**: Optimized for deployment on Google Cloud Run.

## How It Works
1. Users invoke the `/dog_or_cat` command and upload an image.
2. The bot processes the image and validates its format.
3. A TensorFlow model predicts whether the image depicts a dog or a cat.
4. The bot responds in real-time with the classification result.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- A Discord bot token (stored in a `.env` file)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/BLANKatGITHUB/classificationbot.git
   cd classificationbot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your Discord bot token to a `.env` file:
   ```env
   TOKEN=your-bot-token-here
   ```

### Running the Bot
To start the bot, run:
```bash
python main.py
```

### Commands
- `/dog_or_cat`: Upload an image, and the bot will classify it.
- `/hello`: Greet the bot, and it will greet you back.

## Project Structure
- **`main.py`**: Contains bot commands and functionality.
- **`requirements.txt`**: Lists all required dependencies.
- **`base_cat_dog_cnn.keras`**: Pre-trained TensorFlow model for image classification.

## Technologies Used
- **Python**: Core programming language.
- **TensorFlow**: For image classification using a CNN model.
- **Disnake**: Library for creating Discord bots.

## Purpose
This project demonstrates the integration of machine learning into an interactive platform like Discord, making AI accessible and engaging for users.
