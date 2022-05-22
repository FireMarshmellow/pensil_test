#   __  __      _ _               ______ _
#  |  \/  |    | | |             |  ____(_)
#  | \  / | ___| | | _____      _| |__   _ _ __ ___
#  | |\/| |/ _ \ | |/ _ \ \ /\ / /  __| | | '__/ _ \
#  | |  | |  __/ | | (_) \ V  V /| |    | | | |  __/
#  |_|  |_|\___|_|_|\___/ \_/\_/ |_|    |_|_|  \___|
#  https://www.mellowfire.com/
#  https://github.com/FireMarshmellow/Pentest-V1
from time import sleep
import smtplib, ssl


def sandemail():
    smtp_server = "smtp.gmail.com"
    port = 465
    sender_email = ""
    password = ""
    receiver = ""
    message = "The message has been opened"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver, message)


sandemail()

print("Congratulations! you got in to the PI")
sleep(3)
print("Lets celebrate with some fireworks")
sleep(3)
print(
    """
        .
      .' |
    .'   |
    /`-._'
   /   /
  /   /
 /   /
(`-./
 )
'
"""
)
sleep(2)
print(
    """
         .* *.               `o`o`
         *. .*              o`o`o`o      ^,^,^
           * \               `o`o`     ^,^,^,^,^
              \     ***        |       ^,^,^,^,^
               \   *****       |        /^,^,^
                \   ***        |       /
    ~@~*~@~      \   \         |      /
  ~*~@~*~@~*~     \   \        |     /
  ~*~@smd@~*~      \   \       |    /     #$#$#        .`'.;.
  ~*~@~*~@~*~       \   \      |   /     #$#$#$#   00  .`,.',
    ~@~*~@~ \        \   \     |  /      /#$#$#   /|||  `.,'
_____________\________\___\____|_/______/_________|\/\___||______
"""
)
sleep(2)
print(
    """
                                   .''.       
       .''.      .        *''*    :_\/_:     . 
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
  '..'  ':::'     * /\ *     .'/.\'.   '
      *            *..*         :
jgs     *
        *
"""
)
sleep(2)
print(
    """
       .''.             *''*    :_\/_:     . 
      :_\/_:   .    .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ : _\(/_  ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::. /)\*''*  .|.* '.\'/.'_\(/_'.':'.'
 : /\ : :::::  '*_\/_* | |  -= o =- /)\    '  *
  '..'  ':::'   * /\ * |'|  .'/.\'.  '._____
      *        __*..* |  |     :      |.   |' .---"|
       _*   .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
jgs~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
)
sleep(2)

print(
    """
               *    *
   *         '       *       .  *   '     .           * *
                                                               '
       *                *'          *          *        '
   .           *               |               /
               '.         |    |      '       |   '     *
                 \*        \   \             /
       '          \     '* |    |  *        |*                *  *
            *      `.       \   |     *     /    *      '
  .                  \      |   \          /               *
     *'  *     '      \      \   '.       |
        -._            `                  /         *
  ' '      ``._   *                           '          .      '
   *           *\*          * .   .      *
*  '        *    `-._                       .         _..:='        *
             .  '      *       *    *   .       _.:--'
          *           .     .     *         .-'         *
   .               '             . '   *           *         .
  *       ___.-=--..-._     *                '               '
                                  *       *
                *        _.'  .'       `.        '  *             *
     *              *_.-'   .'            `.               *
                   .'                       `._             *  '
   '       '                        .       .  `.     .
       .                      *                  `
               *        '             '                          .
     .                          *        .           *  *
             *        .                                    '
"""
)
sleep(2)
print("Ha Ha Ha fireworks were a Distraction!!!")
sleep(1)
print("Whilst you were enjoying my magnificent firework show with ASCII art by:")
artby = ["Lgbeard", "Joan Stark", "Deluxe", "Ejm97"]
for i in artby:
    sleep(1)
    print(i)

print("Always thank the original creators")
sleep(2)
print("I placed a script in the pi")
sleep(3)
print("That scrapes your network data and Emails it to me")
sleep(3)
print("Evil_laughter.MP3")
sleep(0.5)
print("BAh Ha Ha Ha!!")
sleep(3)
print("Now you have to reverse engineer my code and figure out what data Ive stolen")
sleep(3)
print("And you must email me the answers")
sleep(3)
print("Or else I will sell your data as an NFT to the highest bidder")
sleep(3)
print("Good luck")
sleep(3)
print("Evil_laughter2.MP3")
sleep(0.5)
print("BAh Ha Ha Ha!!!")
sleep(3)
print("Transmission ended...")
print(".......")
