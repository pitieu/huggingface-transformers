import express from "express";
import { pipeline } from "@xenova/transformers";
// List of available models
// https://huggingface.co/models?other=transformers.js&sort=modified

const app = express();
const port = 3000;

app.get("/classify", async (req, res) => {
  try {
    let pipe = await pipeline(
      "text-classification",
      "Xenova/distilbert-base-uncased-finetuned-sst-2-english"
    );
    let out = await pipe("I love transformers!");
    res.json(out);
  } catch (e) {
    console.log(e);
  }
});

app.get("/tag", async (req, res) => {
  try {
    let pipe = await pipeline(
      "image-to-text",
      "Xenova/vit-gpt2-image-captioning"
    );
    let out = await pipe("./assets/3.jpg");
    res.json(out);
  } catch (e) {
    console.log(e);
    res.json({});
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});
