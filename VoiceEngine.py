import azure.cognitiveservices.speech as speechsdk
from mirai import Voice

speech_key = ""
service_region = ""
emotion = 'Cheerful'

def get_voi(response):
    global speech_key
    global service_region
    global emotion

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_synthesis_voice_name = "zh-CN-XiaoxiaoNeural"

    ssml = """<speak version='1.0' xml:lang='zh-CN' xmlns='http://www.w3.org/2001/10/synthesis' xmlns:mstts='http://www.w3.org/2001/mstts'>
         <voice name='zh-CN-XiaoxiaoNeural' style="{}" styledegree="2">
         <prosody rate="-2%" pitch="4%">
                {}
            </prosody>

             </voice>
     </speak>""".format(emotion, response)

    audio_config = speechsdk.audio.AudioOutputConfig(filename="response.wav")
    # use the default speaker as audio output.
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    result = speech_synthesizer.speak_ssml_async(ssml).get()

    # Check result
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(response))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))

    return Voice(path=str('./response.wav'))

