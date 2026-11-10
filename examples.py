""" 
Example program for terminal_pet_respin for demo purposes.

Shows the full lifecycle of the pet from egg to full python. 
"""

from terminal_pet_respin import add_commands, create_egg, draw_pet, get_stage, pet_says

PET_NAME = "Respin"
HATCH_AT = 10


def show(title, art):
    print(f"\n=== {title} ===")
    print(art)


def main():
    pet = create_egg(PET_NAME, hatch_at=HATCH_AT)
    print(f"You found an egg named {pet['name']}! It hatches after {HATCH_AT} commands.")
    show(f"{pet['commands_run']} commands: {pet['stage']}", draw_pet(pet["stage"]))

    # feed the egg commands in batches and watch it grow through every stage.
    for batch in (5, 5, 10, 20):
        add_commands(pet, batch)
        stage = pet["stage"]
        show(f"{pet['commands_run']} commands: {stage}", draw_pet(stage, pet_says(stage)))

    # get_stage works from the numbers alone, without a pet.
    print("\n=== Planning ahead with get_stage (hatch_at=50) ===")
    for commands_run in (0, 25, 50, 100, 200):
        print(f"{commands_run:>3} commands -> {get_stage(commands_run, 50)}")

    # invalid input is rejected with clear errors.
    print("\n=== Error handling ===")
    bad_calls = (
        lambda: create_egg("", hatch_at=HATCH_AT),
        lambda: add_commands(pet, 0),
        lambda: get_stage(-1, HATCH_AT),
        lambda: draw_pet("dragon"),
    )
    for bad_call in bad_calls:
        try:
            bad_call()
        except (TypeError, ValueError) as error:
            print(f"{type(error).__name__}: {error}")


if __name__ == "__main__":
    main()