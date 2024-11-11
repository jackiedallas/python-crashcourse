from faker import Faker  # type: ignore

fake = Faker()
randomNames = [fake.first_name().lower() for _ in range(5)]
randomJobs = [fake.job().lower() for _ in range(5)]

# print(randomNames)
print("\n")
jcount = 0
for name in randomNames:
    if name.startswith('j'):
        jcount += 1
        print(f"{name.title()} starts with a 'J'.")
    else:
        print(f"{name} does not start with a 'J'.")

print(f"We had {jcount} 'J' names that go around!")
print("\n")

print("\n")
for job in randomJobs:
    if (
        'engineer' in job or
        'architect' in job or
        'research' in job or
        'science' in job
    ):
        job_type = 'technical'
    elif 'editor' in job:
        job_type = 'creator'
    elif 'pilot' in job:
        job_type = 'essential'
    else:
        job_type = 'general'

    print(f"{job.title()} is a {job_type.title()} position")
