import os

def generate_invitations(template, attendees):
    # validate inp type
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return
    
    # Check inputs if empty
    if not template:
        print("Error: Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # code
    # Process each attendee
    for idx, attendee in enumerate(attendees, start=1):
        # Replace placeholders with actual values or "N/A" if missing
        output_content = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )

        # output file name
        output_filename = f"output_{idx}.txt"

        # processed template to the output file
        with open(output_filename, 'w') as output_file:
            output_file.write(output_content)

if __name__ == "__main__":
    # Read template from file
    with open('template.txt', 'r') as file:
        template_content = file.read()

    # List of attendees
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
    ]

    # Call function with template and attendees list
    generate_invitations(template_content, attendees)