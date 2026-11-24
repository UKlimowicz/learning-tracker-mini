from tracker import StudySession, LearningTracker


tracker = LearningTracker()

session1 = StudySession("21.11.2026", "SQL", 120)
session2 = StudySession("22.11.2026", "Python", 240)
session3 = StudySession("21.11.2026", "English", 90)
session4 = StudySession("21.11.2026", "SQL", 90)
session5 = StudySession("22.11.2026", "English", 60)
session6 = StudySession("21.11.2026", "Python", 120)
session7 = StudySession("23.11.2026", "Django", 180)
session8 = StudySession("24.11.2026", "Git", 60)
session9 = StudySession("24.11.2026", "English", 45)
session10 = StudySession("24.11.2026", "Pytest", 90)
session11 = StudySession("25.11.2026", "PostgreSQL", 150)
session12 = StudySession("25.11.2026", "Learning Tracker", 120)

tracker.add_session(session1)
tracker.add_session(session2)
tracker.add_session(session3)
tracker.add_session(session4)
tracker.add_session(session5)
tracker.add_session(session6)
tracker.add_session(session7)
tracker.add_session(session8)
tracker.add_session(session9)
tracker.add_session(session10)
tracker.add_session(session11)
tracker.add_session(session12)



print(tracker.total_study_time())
print(tracker.longest_session())
print(tracker.avg_study_time())
print(tracker.session_count())

tracker.save_to_file()
print("Dane zapisane do pliku.")


tracker.load_from_file()
print(tracker.session_count())

