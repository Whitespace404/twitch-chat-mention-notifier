from twitchobserver import Observer
from win10toast import ToastNotifier

channel = input("Channel: ")

with Observer("<twitch-username>", "oauth:__________________________________") as observer:
    observer.join_channel(channel)

    while True:
        try:
            for event in observer.get_events():
                if event.type == 'TWITCHCHATMESSAGE':

                    message = event.message.lower()
                    print(message)

                    if "<the word that you want to get notified for>" in message:
                        n = ToastNotifier()
                        n.show_toast(f"Twitch Chat: {channel}", f"{event.message}", duration = 10)
                        
                if event.type == "TWITCHCHATJOIN":
                    print(event.nickname, "joined.")

                if event.type == "TWITCHCHATLEAVE":
                    print(f"{event.nickname} left.")

        except KeyboardInterrupt:
            observer.leave_channel('channel')
            break
            
