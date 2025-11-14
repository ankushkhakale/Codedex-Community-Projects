Did you know that you can control a game with just your hands? No keyboard, no mouse - just waving at your webcam like you’re living in a sci-fi movie!

In this project tutorial, we’ll build Air Juggler, a webcam gesture-controlled game that uses TensorFlow.js and MediaPipe Hands to detect your hand movements in real-time!

# Setup

The folder should have the following structure:
air-juggler-with-tensorflowjs/
   ├── starter/                  # Start here - incomplete code with TODOs
   │       ├── index.html       # HTML without TensorFlow scripts
   │       ├── style.css        # Complete styling (provided)
   │       ├── game.js          # Game boilerplate with TODOs
   │       └── handTracking.js  # Hand tracking boilerplate with TODOs
   ├── completed/                # Reference - fully working code
   │       ├── index.html
   │       ├── style.css
   │       ├── game.js
   │       └── handTracking.js
   └── README.md

## How to Play

1. **Open the game** - Load `index.html` in a browser (Chrome, Firefox, Edge recommended)
2. **Grant camera permission** - Allow access when prompted
3. **Click "Start Game"** - Wait for the ML model to load (~2-3 seconds)
4. **Move your hands** - Position your hands in front of the camera
5. **Bounce the ball** - Keep the ball in the air by hitting it with your hands!

### Game Rules

- A ball falls due to gravity
- Your hands create invisible "paddles" that bounce the ball upward
- If the ball falls off the bottom of the screen, game over
- Score is based on how long you survive (in seconds)

## Technical Stack

- **HTML5 Canvas** - Game rendering
- **Vanilla JavaScript** - No frameworks needed!
- **TensorFlow.js** - Machine learning framework
- **MediaPipe Hands** - Pre-trained hand detection model

## Performance Notes

- **Detection runs at ~30 FPS** - Good balance of accuracy and performance
- **Rendering runs at 60 FPS** - Smooth visuals
- **Model loading** - First load downloads ~10MB, then cached
- **GPU acceleration** - Automatically used when available

## Troubleshooting

**Camera not working?**

- Ensure you've granted camera permissions
- Check that no other app is using your camera
- Try refreshing the page
- Check browser console for errors

**Hands not detected?**

- Ensure good lighting conditions
- Keep hands clearly visible to camera
- Try moving closer or adjusting camera angle
- Make sure hands are within the camera frame

## Resources

- [TensorFlow.js Documentation](https://www.tensorflow.org/js)
- [MediaPipe Hands Guide](https://google.github.io/mediapipe/solutions/hands.html)
- [Hand Pose Detection API](https://github.com/tensorflow/tfjs-models/tree/master/hand-pose-detection)
- [WebRTC getUserMedia](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia)
- [HTML5 Canvas Tutorial](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial)
- [Huge thanks to Dharmarajsinh Jethva 🙌](https://github.com/Goku-kun/air-juggler-using-tensorflowjs.git)


## Credits

Built as part of the Codédex Project Tutorials