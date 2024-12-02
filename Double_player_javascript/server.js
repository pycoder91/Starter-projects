
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const path = require('path');
const app = express();
app.use(bodyParser.json());

const emptyCollection = async (collectionName) => {
  try {
    if (mongoose.connection.models[collectionName]) {
      await mongoose.connection.models[collectionName].deleteMany({});
      console.log(`Collection '${collectionName}' emptied successfully.`);
    }
  } catch (error) {
    console.error(`Error emptying collection '${collectionName}':`, error);
  }
};


// Connect to MongoDB
mongoose.connect('mongodb://localhost/3d_tic_tac_toe', { useNewUrlParser: true, useUnifiedTopology: true });

// Create a MongoDB schema and model
const cube3DSchema = new mongoose.Schema({
  cube_3d: [[Array]]
});

const Cube3DModel = mongoose.model('Cube3D', cube3DSchema);


app.use('/public', express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

app.get('/single_player_game', (req, res) => {
  res.sendFile(path.join(__dirname, 'single_player_game.html'));
});

app.get('/double_player_game', (req, res) => {
  res.sendFile(path.join(__dirname, 'double_player_game.html'));
});

app.get('/online_player_game', (req, res) => {
  res.sendFile(path.join(__dirname, 'online_player_game.html'));
});

// Handle the POST request to save cube_3d data
app.post('/save_cube_3d/:collectionName', async (req, res) => {
  try {
    const { collectionName } = req.params;

    // Check if the model already exists
    if (mongoose.connection.models[collectionName]) {
      console.log(`Model '${collectionName}' already exists. Skipping creation.`);
    } else {
      // Create the model if it doesn't exist
      const cube3DSchema = new mongoose.Schema({
        cube_3d: [[Array]],
      });

      mongoose.model(collectionName, cube3DSchema);
    }
    await emptyCollection(collectionName);
    const DynamicCube3DModel = mongoose.model(collectionName);
    const cube3DData = req.body.cube_3d;

    const cube3DInstance = new DynamicCube3DModel({ cube_3d: cube3DData });
    await cube3DInstance.save();

    res.status(200).json({ message: 'Cube 3D data saved successfully.' });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.get('/delete_collection/:collectionName', async (req, res) => {
  try {
    const { collectionName } = req.params;

    if (mongoose.connection.models[collectionName]) {
      await mongoose.connection.models[collectionName].collection.drop();
      console.log(`Collection '${collectionName}' deleted successfully.`);
    } else {
      console.log(`Collection '${collectionName}' does not exist.`);
    }

    res.status(200).json({ message: 'Collection deleted successfully.' });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.get('/get_cube_3d/:collectionName', async (req, res) => {
  try {
    const { collectionName } = req.params;
    const DynamicCube3DModel = mongoose.model(collectionName);

    const cube3DData = await DynamicCube3DModel.findOne();
    if (!cube3DData) {
      return res.status(404).json({ error: 'Cube 3D data not found.' });
    }

    res.status(200).json({ cube_3d: cube3DData.cube_3d });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});


const port = 3000; 
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

