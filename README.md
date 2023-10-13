# DS5111_FALL2023_SW2_Lab

All three seem to work fine now:
- Make `env`:
![alt text](https://github.com/allaccountstaken/DS5111_FALL2023_SW2_Lab/blob/tdd_second_decorator/make%20env.png)

-Make `run`:
![alt text](https://github.com/allaccountstaken/DS5111_FALL2023_SW2_Lab/blob/tdd_second_decorator/make%20run.png)

-Make `tests`:
![alt text](https://github.com/allaccountstaken/DS5111_FALL2023_SW2_Lab/blob/tdd_second_decorator/make%20tests.png)

Additional questions:
1. I had to update the default ubuntu installation that came with my AWS machine.
2. Ubuntu systems, you need to install the python3-venv package using the following command: apt install python3.10-ven. That was not clear at all, and I had to read multiple blog posts about this.
3. Because we need to maintaite the state. Otherwise every command is treated as a new shell.
4. I was reaserching the issue and possible make -B <target> could work?
5. To be able to import `clockdeco_param`logic
