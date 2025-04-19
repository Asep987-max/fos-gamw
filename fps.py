# Game FPS Text-Based by GitHub
import random

player = {"health": 100, "ammo": 30}
enemies = [{"health": 30} for _ in range(3)]

def show_game():
    print(f"\n❤️ Health: {player['health']} | 🔫 Ammo: {player['ammo']}")
    print("\nEnemies ahead!" if enemies else "Area clear!")

while player['health'] > 0 and enemies:
    show_game()
    cmd = input("\n[W]Move [S]Shoot [Q]Quit: ").upper()
    
    if cmd == "W":
        print("You move forward!")
        if random.random() < 0.3:
            print("Found ammo! +10 bullets")
            player["ammo"] += 10
    elif cmd == "S" and player["ammo"] > 0:
        player["ammo"] -= 1
        dmg = random.randint(5, 15)
        enemies[0]["health"] -= dmg
        print(f"You deal {dmg} damage!")
        
        if enemies[0]["health"] <= 0:
            print("Enemy defeated!")
            enemies.pop(0)
    elif cmd == "Q":
        break

print("\nGame Over!" if player['health'] <=0 else "You win!")
