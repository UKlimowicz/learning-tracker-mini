
class StudySession:

    def __init__(self, date, topic, duration):
        self.date = date
        self.topic = topic
        self.duration = duration

    def __str__(self):
        return f"{self.date} | {self.topic} | {self.duration} min"


class LearningTracker:

    def __init__(self):
        self.sessions = []

    def add_session(self, session):
        self.sessions.append(session)

    def show_sessions(self):
        for session in self.sessions:
            print(session)

    def total_study_time(self):
        total = 0
        for session in self.sessions:
            total += session.duration

        return total 

    def session_count(self):
        return len(self.sessions)

    def avg_study_time(self):
       return self.total_study_time() / self.session_count()

    def longest_session(self):
        longest = self.sessions[0]

        for session in self.sessions:
            if session.duration > longest.duration:
                longest = session

        return  longest

    def save_to_file(self):
        with open("study_session.txt", "w", encoding = "utf-8") as file:
            for session in self.sessions:
                file.write(f"{session.date} | {session.topic} | {session.duration}\n")

    def load_from_file(self):
        loaded_sessions = []

        with open("study_session.txt", "r", encoding = "utf-8") as file:
            for line in file:
                date, topic, duration_text = line.strip().split(" | ")
                duration = int(duration_text)

                session = StudySession(date, topic, duration)

                loaded_sessions.append(session)

        self.sessions = loaded_sessions
    


