import edge_tts

async def generate_audio(text,outputFilename):
    communicate = edge_tts.Communicate(text,"en-US-AriaNeural")
    await communicate.save(outputFilename)
