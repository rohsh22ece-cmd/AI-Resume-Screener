from pdf_parser import extract_text_from_pdf
from vector_store import add_resume, search_resume

def resume_interactive():
    while True:
        print("\n1. Index Resume")
        print("2. Search Resume")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            pdf_path = input("Enter PDF path: ")
            text = extract_text_from_pdf(pdf_path)
            add_resume(pdf_path, text)
            print("Resume indexed successfully!")

        elif choice == "2":
            job_description = input("Enter job description: ")
            results = search_resume(job_description)

            print("\nTop Matches:")
            for res in results:
                print(f"ID: {res[0]}")
                print(f"Score: {res[1]}")
                print("-" * 40)

        elif choice == "3":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    resume_interactive()
