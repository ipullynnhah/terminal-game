from random import randint, choice

POWER_FACTOR = 5
level = 0
hp = randint(80, 120)
mistakes = 0

print("~" * 28)
print("꩜ Labyrinth of Dimensions ꩜")
print("~" * 28)

print("🏆 GOAL: Reach Level 7! 🏆")
print("\n🧭 VALID MOVE COMMANDS:"
      "\n꩜ [N]orth | [S]outh | [E]ast | [W]est")
print("\n⚔️ VALID FIGHT COMMANDS:"
      "\n꩜ [R]ock | [P]aper | [S]cissors")

print(
  "\n⚠️ WARNING: "
  "\n꩜ Make one choice per level and survive."
  "\n꩜ Each mistake costs you HP, and the consequences worsen with each error!")

while level < 7 and hp > 0:
  level += 1
  power = POWER_FACTOR * level

  print()
  display = f"LEVEL: {level} | HP: {hp}"
  print("~" * len(display))
  print(f"{display}")
  print("~" * len(display))

  move = input("\nMOVE COMMAND: [N·S·E·W] ").lower()
  if move == "north" or move == "n":
    print("Going 👆")
  elif move == "south" or move == "s":
    print("Going 👇")
  elif move == "east" or move == "e":
    print("Going 👉")
  elif move == "west" or move == "w":
    print("Going 👈")
  else:
    mistakes += 1
    lost_hp = level * randint(0, power // 2 * mistakes)
    hp -= lost_hp
    print("Invalid MOVE COMMAND!")
    print(f'You loose {lost_hp} HP.')

  player = input("\nFIGHT COMMAND: [R·P·S] ").lower()
  enemy = choice("rps")

  if player not in ("rock", "r", "paper", "p", "scissors", "s"):
    mistakes += 1
    lost_hp = level * randint(0, power // 2 * mistakes)
    hp -= lost_hp
    print("\nInvalid FIGHT COMMAND!")
    print(f"You loose {lost_hp} HP. I'm choosing for you!")
    player = choice("rps")

  if player == "r" or player == "rock":
    player = "r"
    player_emoji = "🪨"
  elif player == "p" or player == "paper":
    player = "p"
    player_emoji = "📄"
  else:
    player = "s"
    player_emoji = "✂️"

  if enemy == "r":
    enemy_emoji = "🪨"
  elif enemy == "p":
    enemy_emoji = "📄"
  else:
    enemy_emoji = "✂️"

  print(f"\nP: {player_emoji} 🆚 E: {enemy_emoji}")

  if enemy == player:
    status = 0
  elif player == "r":
    if enemy == "s":
      status = 1
    else:
      status = -1
  elif player == "p":
    if enemy == "s":
      status = -1
    else:
      status = 1
  else:
    if enemy == "p":
      status = 1
    else:
      status = -1

  if status == 0:
    print("You drink a random potion! 🍵")
    potion = randint(-power // 2, power // 2)
  elif status == 1:
    potion = randint(0, power)
  else:
    potion = randint(-power, 0)

  if potion < 0:
    print(f"Uh oh! ☠️ That's poison, and you've lost {abs(potion)} HP!")
  elif potion == 0:
    print("Just water. 💧 No effect!")
  else:
    print(f"A healing potion! You gain {potion} HP!")

  hp = min(hp + potion, 120)

if hp > 0:
  print("\n🏆 Congratulations! You've conquered the Labyrinth! 🏆")
else:
  print(f"\n😔 Defeat... You made it to level {level}, but the Labyrinth has bested you.")
