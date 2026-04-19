from datetime import date

def log_workout():
    today = date.today().strftime('%d.%m.%Y')
    print(f'\n=== Workout {today} ===')


    warmup = input('Warmup and streching completed? (yes/no): ')

    day = input('Training day (A/B/C): ').upper()

    exercises = []
    print('\nEnter exercises. Leave name empty to finish.\n')
    while True:
        name = input('Exercise name: ')
        if name == '':
            break
        reps = input('Reps (e.g. 8+8+8+7): ')
        weight = input('Weight (e.g. 9+9+6 or 9 or 0): ')
        rest = input('Rest (min): ')
        note = input('Note (or Enter to skip this): ')
        exercises.append({
            'name': name,
            'reps': reps,
            'weight': weight,
            'rest': rest, 
            'note': note,
        })
        print('Okay Added\n')

        print('\n=== Workout Summary ===')
        print(f'Date: {today} | Day: {day} | Warmup: {warmup}')
        for ex in exercises:
            print(f'- {ex['name']}: {ex['reps']} | {ex['weight']}kg | rest {ex['rest']}min')
            if ex['note']:
                print(f' Note: {ex['note']}')

log_workout()