import argparse
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound

def main():
    parser = argparse.ArgumentParser(description="Extract auto-generated transcript from a YouTube video.")
    parser.add_argument('--video_id', required=True, help='The YouTube video ID (e.g., irmOc3MCKqo)')
    parser.add_argument('--lang', default='es', help='Language code (default: es for Spanish)')
    parser.add_argument('--output', default='transcription.txt', help='output file name')
    args = parser.parse_args()

    try:
        # Intentar obtener el transcript generado automáticamente en el idioma deseado
        transcript = YouTubeTranscriptApi.get_transcript(args.video_id, languages=[args.lang])

        # Unir el transcript en texto plano
        full_text = "\n".join([entry['text'] for entry in transcript])

        # Guardar en un archivo
        filename = f"transcript_{args.output}_{args.lang}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(full_text)

        print(f"✅ Transcript saved to {filename}")

    except TranscriptsDisabled:
        print("❌ Error: Transcripts are disabled for this video.")
    except NoTranscriptFound:
        print(f"❌ Error: No transcript found in the '{args.lang}' language.")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")

if __name__ == "__main__":
    main()
