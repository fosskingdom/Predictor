"""

Author: Mohamed Fariz
Version: 2023.06.20
Application Name: Predictor

It is a supervised machine learning algorithm to predict the future data.

"""

# pylint: disable=C0302


def predict(x_val: float) -> None:
    """
    predict function is used to predict the value by using the equation of (y = mx + b)
    """

    return coef_var.get() * x_val + intercept_var.get()


def time_stat() -> None:
    """
    time_stat function is used to display the current time.
    """

    clock: str = strftime("%I:%M:%S %p")

    time_lbl.configure(text=f"{whoami.title()} @ {clock}")
    time_lbl.update()
    time_lbl.after(ms=1000, func=time_stat)


def cpu_stat():
    """
    cpu_stat function is used to update the cpu running percentage.
    """

    cpu: float = cpu_percent()

    red: int = round(cpu * 2.55)
    green: int = 255 - red

    cpu_lbl.configure(text=f"CPU: {cpu}%", fg_color=f"#{red:02x}{green:02x}00")
    cpu_lbl.update()
    cpu_lbl.after(ms=1000, func=cpu_stat)


def mem_stat():
    """
    mem_stat function is used to update the memory usage in percentage.
    """
    mem: float = virtual_memory().percent

    red: int = round(mem * 2.55)
    green: int = 255 - red

    mem_lbl.configure(text=f"MEM: {mem}%", fg_color=f"#{red:02x}{green:02x}00")
    mem_lbl.update()
    mem_lbl.after(ms=1000, func=mem_stat)


def pwr_stat():
    """
    pwr_stat function is used to update the battery percentage.
    """

    try:
        pwr_float: float = round(sensors_battery().percent, 1)
        pwr: int = int(pwr_float)

        green: int = int(pwr * 2.55)
        red: int = 255 - green

        pwr_lbl.config(text=f"PWR: {pwr_float}%", bg=f"#{red:02x}{green:02x}00")
        pwr_lbl.update()
        pwr_lbl.after(ms=1000, func=pwr_stat)

    except AttributeError:
        pass


def greeting_message() -> None:
    """
    greeting_message function is used to print the greeting message on the console screen.
    """

    clrscr()
    print(F_BLUE + "=" * 80)
    figlet_banner(font=selected_figlet_font)
    print(F_BLUE + "=" * 80)
    print(f"{F_GREEN}{S_BRIGHT}Hello {whoami.title()}, Welcome to Predictor")
    print(
        f"{F_GREEN}{S_BRIGHT}Created by FOSS Kingdom / "
        f"Made with Love {BEATING_HEART} in Incredible India {IND}"
    )
    print(F_BLUE + "=" * 80)


def check_hash(path: str, hash_val: str) -> None:
    """
    check_hash function is used to check the hash digest value of a file
    """

    if not isfile(path=path):
        clrscr()
        print(F_BLUE + "=" * 80)
        print(f"[ERROR]\t[{datetime.now()}]\tFile not found!!")
        print(F_BLUE + "=" * 80)
        terminate()

    if sha256(Path(path).read_bytes()).hexdigest() != hash_val:
        clrscr()
        print(F_BLUE + "=" * 80)
        print(f"[ERROR]\t[{datetime.now()}]\t{path} is corrupted!!")
        print(F_BLUE + "=" * 80)
        terminate()


def toggle_grid_lines() -> None:
    """
    toggle_grid_lines function is used to show/hide grid lines in the graph area
    """

    if grid_var.get() == 1:
        graph.grid(visible=False)
        graph.grid(visible=True, axis=Y)
        fig.canvas.draw()

    if grid_var.get() == 2:
        graph.grid(visible=False)
        graph.grid(visible=True, axis=X)
        fig.canvas.draw()

    if grid_var.get() == 3:
        graph.grid(visible=False)
        graph.grid(visible=True, axis=BOTH)
        fig.canvas.draw()

    if grid_var.get() == 4:
        graph.grid(visible=False)
        fig.canvas.draw()


def dark_theme() -> None:
    """
    dark_theme function is used to set the dark theme interface.
    """

    set_appearance_mode("dark")
    menu_bar.configure(bg="grey", fg=WHITE)
    file_menu.configure(bg="grey", fg=WHITE)
    predict_menu.configure(bg="grey", fg=WHITE)
    goto_menu.configure(bg="grey", fg=WHITE)
    preferences_menu.configure(bg="grey", fg=WHITE)
    grid_menu.configure(bg="grey", fg=WHITE)
    themes_menu.configure(bg="grey", fg=WHITE)
    links_menu.configure(bg="grey", fg=WHITE)
    help_menu.configure(bg="grey", fg=WHITE)
    lbl_frame_1.configure(bg=THEME_COLOR["dark"])
    graph_text_color.set(value=WHITE)
    set_graph_labels()
    graph.figure.set_facecolor(color=BLACK)
    graph.set_facecolor(color=BLACK)
    graph.spines[LEFT].set_color(c="#F00")
    graph.spines[BOTTOM].set_color(c="#00F")

    for _ in [X, Y]:
        graph.tick_params(axis=_, colors=ORANGE)

    fig.canvas.draw()

    lbl_frame_2.configure(bg=THEME_COLOR["dark"])
    lbl_frame_3.configure(bg=THEME_COLOR["dark"])
    popup_menu.configure(bg="grey", fg=WHITE)


def light_theme() -> None:
    """
    light_theme function is used to set the light theme interface.
    """

    set_appearance_mode("light")
    menu_bar.configure(bg="#d9d9d9", fg=BLACK)
    file_menu.configure(bg="#d9d9d9", fg=BLACK)
    predict_menu.configure(bg="#d9d9d9", fg=BLACK)
    goto_menu.configure(bg="#d9d9d9", fg=BLACK)
    preferences_menu.configure(bg="#d9d9d9", fg=BLACK)
    grid_menu.configure(bg="#d9d9d9", fg=BLACK)
    themes_menu.configure(bg="#d9d9d9", fg=BLACK)
    links_menu.configure(bg="#d9d9d9", fg=BLACK)
    help_menu.configure(bg="#d9d9d9", fg=BLACK)
    lbl_frame_1.configure(bg=WHITE)
    graph_text_color.set(value=BLACK)
    set_graph_labels()
    graph.figure.set_facecolor(color=WHITE)
    graph.set_facecolor(color=WHITE)
    graph.spines[LEFT].set_color(c=BLACK)
    graph.spines[BOTTOM].set_color(c=BLACK)

    for _ in [X, Y]:
        graph.tick_params(axis=_, colors=BLACK)

    fig.canvas.draw()
    lbl_frame_2.configure(bg=WHITE)
    lbl_frame_3.configure(bg=WHITE)
    popup_menu.configure(bg="#d9d9d9", fg=BLACK)


def configure_theme_color() -> None:
    """
    configure_theme_color function is used to update the theme color based on the used choice.
    """

    if theme_var.get() == 1:
        dark_theme()

    if theme_var.get() == 2:
        light_theme()

    if theme_var.get() == 3:
        if isDark():
            dark_theme()

        if isLight():
            light_theme()


def special_day_banner(msg: str) -> None:
    """
    special_day_banner function is used to display about the event of the day
    """

    print(f"{F_YELLOW}{S_BRIGHT}Today is {msg}")

    special_day_lbl: CTkLabel = CTkLabel(
        master=app, text=f"Today is {msg}", fg_color="yellow", text_color=BLACK
    )
    special_day_lbl.pack(fill=X)


def exit_app() -> None:
    """
    exit_app function used to exit the tkinter application
    """

    play(path=join(base_path, "./mp3/button-124476.mp3"))

    app.withdraw()

    if askyesno(title="Predictor", message="Are you sure do you really want to quit?"):
        app.quit()
        clr_cache()
        print(F_GREEN + S_BRIGHT + "Bye!!")
        terminate()

    else:
        app.deiconify()
        return None


def clrscr() -> None:
    """
    clear_screen function is used to clear the console screen
    """

    if uname == "posix":
        terminal(command="clear")

    if uname == "nt":
        terminal(command="cls")


def set_title() -> None:
    """
    set_title function is used to set the title name in CLI console.
    """

    if uname == "posix":
        stat: int = terminal(command=f"xtitle -q Predictor {__version__}")

        if stat == 32512:
            # sh: 1: xtitle: not found
            # 32512

            print(f"{F_RED}{S_BRIGHT}Use the following command to install xtitle:")
            print(f"{F_BLUE}{S_BRIGHT}sudo apt update && sudo apt install xtitle -y")

    if uname == "nt":
        terminal(command="title Predictor")


def set_graph_labels() -> None:
    """
    set_graph_labels function is used to set the graph labels like title, x-axis and y-axis with
    the color code.
    """

    fig.suptitle(t=graph_title_var.get(), color=graph_text_color.get())
    fig.supxlabel(t=x_label_var.get(), color=graph_text_color.get())
    fig.supylabel(t=y_label_var.get(), color=graph_text_color.get())


def clr_cache() -> None:
    """
    clear_cache function is used to delete the pycache folder
    """

    cache_dir: str = join(base_path, "__pycache__")

    if isdir(s=cache_dir):
        print(f"[INFO]\t[{datetime.now()}]\tClearing cache files, Please wait...")
        rmtree(path=cache_dir)


def figlet_banner(font: str) -> None:
    """
    figlet_banner function is used to print the figlet text on console
    """

    print()
    print(F_RED + S_BRIGHT + figlet_format(text="Predictor", font=font))
    print()
    print(f"{F_BLUE}Figlet Font: {font}")


def load_tab_1() -> None:
    """
    load_tab_1 function is used to load the graph tab view
    """

    graph_title_var.set(value="Loading...")
    x_label_var.set(value="Loading...")
    y_label_var.set(value="Loading...")

    set_graph_labels()

    graph.cla()
    toggle_grid_lines()
    fig.canvas.draw()


def load_tab_2() -> None:
    """
    load_tab_2 function is used to load the data tab view
    """

    tot_data_lbl.configure(text="Loading...")
    min_val_lbl.configure(text="Loading...")
    avg_val_lbl.configure(text="Loading...")
    max_val_lbl.configure(text="Loading...")
    coef_lbl.configure(text="Loading...")
    intercept_lbl.configure(text="Loading...")
    accuracy_lbl.configure(text="Loading...")
    tomorrow_lbl.configure(text="Loading...")
    next_week_lbl.configure(text="Loading...")
    next_month_lbl.configure(text="Loading...")
    next_year_lbl.configure(text="Loading...")
    stat_lbl.configure(text="Loading...", text_color="purple")
    last_update_lbl.configure(text="Loading...")

    src_btn.configure(state=DISABLED)
    google_play_btn.configure(state=DISABLED)


def load_tab_3() -> None:
    """
    load_tab_3 function is used to load the info tab view
    """

    txt_box.configure(state=NORMAL)
    txt_box.delete(index1="1.0", index2=END)
    txt_box.unbind(sequence="<Button-1>")
    txt_box.insert(index="1.0", text="Loading, Please wait...")
    txt_box.configure(state=DISABLED)

    for _ in ["<Button-3>", "<Control-C>", "<Control-c>"]:
        txt_box.unbind(_)


def loading_ui(value: int) -> None:
    """
    loading_ui function is used to load the user interface.
    """

    greeting_message()

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Loading, Please wait..."
    )

    for _ in ["<Control-R>", "<Control-r>", "<Control-S>", "<Control-s>"]:
        app.unbind(sequence=_)

    for _ in ["Clear", "Refresh", "Download CSV"]:
        file_menu.entryconfig(_, state=DISABLED)

    header_lbl.configure(text="Loading, Please wait...")

    choice.set(value=value)
    rb1.configure(state=DISABLED)
    rb2.configure(state=DISABLED)

    clear_btn.configure(state=DISABLED)
    refresh_btn.configure(state=DISABLED)
    dl_btn.configure(state=DISABLED)
    exit_btn.configure(state=DISABLED)

    load_tab_1()
    load_tab_2()
    load_tab_3()

    progress_value.set(value=0)
    progress_bar.configure(progress_color="#F00")
    percentage_lbl.configure(text="0.00%")

    footer_lbl.configure(text="Loading, Please wait...")

    app.update()


def update_progress_bar(var: float) -> None:
    """
    update_progress_bar function is used to update the progress bar dynamically.
    """

    progress_value.set(value=var)

    green: int = round(progress_value.get() * 255)
    red: int = 255 - green

    progress_bar.configure(progress_color=f"#{red:02x}{green:02x}00")
    percentage_lbl.configure(
        text=f"{round(number=progress_value.get() * 100, ndigits=2)}%"
    )
    progress_bar.update()


def predict_linear_y_axis(linear_y_axis: list, x_axis, y_axis) -> None:
    """
    predict_linear_y_axis function is used to predict the linear line between the data.
    """

    model.fit(x_axis, y_axis)

    coef_var.set(value=float(model.coef_))
    intercept_var.set(value=float(model.intercept_))

    for _ in tqdm(iterable=range(1, tot_var.get() + 1)):
        linear_y_axis.append(float(model.predict(X=[[_]])))
        percentage: float = _ / tot_var.get()
        update_progress_bar(var=percentage)

    update_progress_bar(var=0)

    print(F_BLUE + "=" * 80)


def draw_graph(linear_y_axis: list, x_axis, y_axis, data) -> None:
    """
    draw_graph function is used to plot the graph on application
    """

    tfig = figure()
    padding = (80 - len(graph_title_var.get())) // 2
    print(F_RED + S_BRIGHT + " " * padding + graph_title_var.get())

    tfig.plot(data["sl.no"], data["price"])
    # tfig.plot(data["sl.no"], linear_y_axis)
    tfig.show()

    print(F_BLUE + "=" * 80)

    if choice.get() == 1:
        graph_title_var.set(value="USD/INR Exchange Rates Prediction")
        x_label_var.set(value="Total no of Days")
        y_label_var.set(value="USD/INR rate (₹)")

    if choice.get() == 2:
        graph_title_var.set(value="e-Gold Price Predictor")
        x_label_var.set(value="Total no of Days")
        y_label_var.set(value="Price in INR (₹)")

    set_graph_labels()

    graph.plot(x_axis, y_axis, "--", label="Original data")
    update_progress_bar(var=0.16)

    graph.plot(x_axis, linear_y_axis, "--", label="Predicted data")
    update_progress_bar(var=0.32)

    x_axis_new = x_axis[-1] + 1
    y_axis_new = model.predict(X=[x_axis_new])
    graph.scatter(x=x_axis_new, y=y_axis_new, label="Tomorrow expected")
    update_progress_bar(var=0.48)

    x_axis_new = x_axis[-1] + 7
    y_axis_new = model.predict(X=[x_axis_new])
    graph.scatter(x=x_axis_new, y=y_axis_new, label="Next week expected")
    update_progress_bar(var=0.64)

    x_axis_new = x_axis[-1] + 30.4375
    y_axis_new = model.predict(X=[x_axis_new])
    graph.scatter(x=x_axis_new, y=y_axis_new, label="Next month expected")
    update_progress_bar(var=0.8)

    x_axis_new = x_axis[-1] + 365.25
    y_axis_new = model.predict(X=[x_axis_new])
    graph.scatter(x=x_axis_new, y=y_axis_new, label="Next year expected")
    update_progress_bar(var=1)

    graph.legend()
    fig.canvas.draw()

    update_progress_bar(var=0)

    app.update()


def display_data(date_list, ndigits) -> None:
    """
    display_data function is used to display the data to the application.
    """

    print(f"{S_BRIGHT}Total Records (n): {tot_var.get()}")
    tot_data_lbl.configure(text=tot_var.get())
    update_progress_bar(var=0.07)

    print(f"{S_BRIGHT}Minimum: {min_var.get()}")
    min_val_lbl.configure(text=f"₹ {min_var.get()}")
    update_progress_bar(var=0.14)

    print(f"{S_BRIGHT}Average: {round(number=avg_var.get(), ndigits=ndigits)}")
    avg_val_lbl.configure(text=f"₹ {round(number=avg_var.get(), ndigits=ndigits)}")
    update_progress_bar(var=0.21)

    print(f"{S_BRIGHT}Maximum: {max_var.get()}")
    max_val_lbl.configure(text=f"₹ {max_var.get()}")
    update_progress_bar(var=0.28)

    print(f"{S_BRIGHT}Coefficient (m): {round(number=coef_var.get(), ndigits=ndigits)}")
    coef_lbl.configure(text=round(number=coef_var.get(), ndigits=ndigits))
    update_progress_bar(var=0.35)

    print(
        f"{S_BRIGHT}Intercept (b): {round(number=intercept_var.get(), ndigits=ndigits)}"
    )
    intercept_lbl.configure(text=round(number=intercept_var.get(), ndigits=ndigits))
    update_progress_bar(var=0.42)

    print(f"{S_BRIGHT}Accuracy: {round(number=accuracy_var.get(), ndigits=2)}%")
    accuracy_lbl.configure(text=f"{round(number=accuracy_var.get(), ndigits=2)}%")
    update_progress_bar(var=0.49)

    print(
        f"{S_BRIGHT}Tomorrow expected: {round(number=tomorrow_var.get(), ndigits=ndigits)}"
    )
    tomorrow_lbl.configure(
        text=f"₹ {round(number=tomorrow_var.get(), ndigits=ndigits)}"
    )
    update_progress_bar(var=0.56)

    print(
        f"{S_BRIGHT}Next week expected: {round(number=next_week_var.get(), ndigits=ndigits)}"
    )
    next_week_lbl.configure(
        text=f"₹ {round(number=next_week_var.get(), ndigits=ndigits)}"
    )
    update_progress_bar(var=0.63)

    print(
        f"{S_BRIGHT}Next month expected: {round(number=next_month_var.get(), ndigits=ndigits)}"
    )
    next_month_lbl.configure(
        text=f"₹ {round(number=next_month_var.get(), ndigits=ndigits)}"
    )
    update_progress_bar(var=0.7)

    print(
        f"{S_BRIGHT}Next year expected: {round(number=next_year_var.get(), ndigits=ndigits)}"
    )
    next_year_lbl.configure(
        text=f"₹ {round(number=next_year_var.get(), ndigits=ndigits)}"
    )
    update_progress_bar(var=0.77)

    if coef_var.get() < 0:
        print(f"{S_BRIGHT}Status: BEAR {DOWN_ARROW}")
        stat_lbl.configure(text=f"BEAR {DOWN_ARROW}", text_color=RED)

    elif coef_var.get() > 0:
        print(f"{S_BRIGHT}Status: BULL {UP_ARROW}")
        stat_lbl.configure(text=f"BULL {UP_ARROW}", text_color="green")

    else:
        print(f"{S_BRIGHT}Status: No Change")
        stat_lbl.configure(text="No Change", text_color=ORANGE)

    update_progress_bar(var=0.84)

    last_updated_date: str = list(date_list)[-1]
    print(f"{S_BRIGHT}Last updated: {last_updated_date}")
    last_update_lbl.configure(text=last_updated_date)
    update_progress_bar(var=0.91)

    print(F_BLUE + "=" * 80)

    if choice.get() == 1:
        src_btn.configure(
            state=NORMAL,
            command=lambda: browser(url="https://www.google.com/finance/quote/USD-INR"),
        )
        google_play_btn.configure(state=DISABLED)

    if choice.get() == 2:
        src_btn.configure(
            state=NORMAL,
            command=lambda: browser(url="https://www.mmtcpamp.com/"),
        )
        google_play_btn.configure(
            state=NORMAL,
            command=lambda: browser(
                url="https://play.google.com/store/apps/details?id=com.mmtcpamp.app"
            ),
        )

    update_progress_bar(var=1)

    app.update()


def display_info() -> None:
    """
    display_info function is used to display the information on the text widget.
    """

    txt_box.configure(state=NORMAL)
    txt_box.delete(index1="1.0", index2=END)
    txt_box.unbind(sequence="<Button-1>")

    if choice.get() == 1:
        with open(
            file=join(base_path, "./docs/USD_2_INR.txt"), mode="r", encoding="utf-8"
        ) as file:
            txt_box.insert(index="1.0", text=file.read())

            txt_box.tag_add(tagName="hyperlink_1", index1="11.0", index2="11.50")
            txt_box.tag_add(tagName="hyperlink_2", index1="12.0", index2="12.42")

            for _ in ["hyperlink_1", "hyperlink_2"]:
                txt_box.tag_config(tagName=_, foreground=BLUE, underline=True)
                txt_box.tag_bind(
                    tagName=_,
                    sequence="<Enter>",
                    func=lambda event: txt_box.configure(cursor="hand2"),
                )
                txt_box.tag_bind(
                    tagName=_,
                    sequence="<Leave>",
                    func=lambda event: txt_box.configure(cursor="xterm"),
                )

            txt_box.tag_bind(
                tagName="hyperlink_1",
                sequence="<Button-1>",
                func=lambda event: browser(
                    url="https://en.wikipedia.org/wiki/United_States_dollar"
                ),
            )
            txt_box.tag_bind(
                tagName="hyperlink_2",
                sequence="<Button-1>",
                func=lambda event: browser(
                    url="https://en.wikipedia.org/wiki/Indian_rupee"
                ),
            )

            file.close()

    if choice.get() == 2:
        with open(
            file=join(base_path, "./docs/24k_e-Gold.txt"), mode="r", encoding="utf-8"
        ) as file:
            txt_box.insert(index="1.0", text=file.read())
            txt_box.tag_add(tagName="hyperlink_3", index1="96.0", index2="96.47")
            txt_box.tag_config(tagName="hyperlink_3", foreground=BLUE, underline=True)
            txt_box.tag_bind(
                tagName="hyperlink_3",
                sequence="<Enter>",
                func=lambda event: txt_box.configure(cursor="hand2"),
            )
            txt_box.tag_bind(
                tagName="hyperlink_3",
                sequence="<Leave>",
                func=lambda event: txt_box.configure(cursor="xterm"),
            )
            txt_box.tag_bind(
                tagName="hyperlink_3",
                sequence="<Button-1>",
                func=lambda event: browser(
                    url="https://www.mmtcpamp.com/gold-silver-rate-today"
                ),
            )

            file.close()

    txt_box.configure(state=DISABLED)

    txt_box.bind(
        "<Button-3>", lambda event: popup_menu.tk_popup(x=event.x_root, y=event.y_root)
    )

    for _ in ["<Control-C>", "<Control-c>"]:
        txt_box.bind(_, lambda event: copy_to_clipboard())

    app.update()


def reset_tab_1() -> None:
    """
    reset_tab_1 function is used to reset the graph tab view
    """

    graph_title_var.set(value="Graph Area")
    x_label_var.set(value="X-Axis")
    y_label_var.set(value="Y-Axis")

    set_graph_labels()

    graph.cla()
    toggle_grid_lines()
    fig.canvas.draw()


def reset_tab_2() -> None:
    """
    reset_tab_2 function is used to teset the data tab view
    """

    tot_var.set(value=0)
    min_var.set(value=0)
    avg_var.set(value=0)
    max_var.set(value=0)
    coef_var.set(value=0)
    intercept_var.set(value=0)
    accuracy_var.set(value=0)
    tomorrow_var.set(value=0)
    next_week_var.set(value=0)
    next_month_var.set(value=0)
    next_year_var.set(value=0)

    tot_data_lbl.configure(text=tot_var.get())
    min_val_lbl.configure(text=min_var.get())
    avg_val_lbl.configure(text=avg_var.get())
    max_val_lbl.configure(text=max_var.get())
    coef_lbl.configure(text=coef_var.get())
    intercept_lbl.configure(text=intercept_var.get())
    accuracy_lbl.configure(text=f"{accuracy_var.get()}%")
    tomorrow_lbl.configure(text=tomorrow_var.get())
    next_week_lbl.configure(text=next_week_var.get())
    next_month_lbl.configure(text=next_month_var.get())
    next_year_lbl.configure(text=next_year_var.get())
    stat_lbl.configure(text="N/A", text_color="purple")
    last_update_lbl.configure(text="N/A")

    src_btn.configure(state=DISABLED)
    google_play_btn.configure(state=DISABLED)


def reset_tab_3() -> None:
    """
    reset_tab_3 function is used to reset the info tab view
    """

    txt_box.configure(state=NORMAL)
    txt_box.delete(index1="1.0", index2=END)
    txt_box.unbind(sequence="<Button-1>")
    txt_box.insert(index="1.0", text=f"No information available ({INFORMATION})...")
    txt_box.configure(state=DISABLED)

    for _ in ["<Button-3>", "<Control-C>", "<Control-c>"]:
        txt_box.unbind(sequence=_)


def reset_ui():
    """
    reset_ui function is used to reset the user interface
    """

    greeting_message()

    play(path=join(base_path, "./mp3/fh_paper_swipe_surface2_short_01wav-14432.mp3"))

    for _ in ["<Control-R>", "<Control-r>", "<Control-S>", "<Control-s>"]:
        app.unbind(sequence=_)

    for _ in ["Clear", "Refresh", "Download CSV"]:
        file_menu.entryconfig(_, state="disabled")

    header_lbl.configure(text=f"Hello {whoami.title()}, Welcome to Predictor")

    rb1.configure(state=NORMAL)
    rb2.configure(state=NORMAL)
    choice.set(value=0)

    clear_btn.configure(state=DISABLED)
    refresh_btn.configure(state=DISABLED, text="Refresh")
    dl_btn.configure(state=DISABLED)
    exit_btn.configure(state=NORMAL)

    reset_tab_1()
    reset_tab_2()
    reset_tab_3()

    footer_lbl.configure(
        text="Created by FOSS KINGDOM / Made with Love in Incredible India."
    )

    app.update()


def usd2inr() -> None:
    """
    usd_to_inr function is used to predict the USD to INR value
    """

    loading_ui(value=1)
    update(data=read_db(url=USD2INR))


def e_gold_24k() -> None:
    """
    e_gold_24 function is used to predict the 24K e-Gold Price
    """

    loading_ui(value=2)
    update(data=read_db(url=E_GOLD))


def read_db(url: str):
    """
    read_database function is used to read the csv file from the internet.
    """

    try:
        print(
            f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
            f"{S_RESET_ALL}]\t{S_BRIGHT}Reading database, Please wait..."
        )

        with urlopen(url, timeout=10) as response:
            data: read_csv = read_csv(
                filepath_or_buffer=response,
                encoding="utf-8",
                parse_dates=["date"],
                date_format="%d/%m/%Y",
            )
            response.close()

            tot_var.set(value=len(data))

            return data

    except URLError as url_error:
        reset_ui()

        print(
            f"{S_BRIGHT}Failed to read database file. Please chech your internet connection..."
        )
        print(f"{S_BRIGHT}Error Code: urllib.error.URLError")
        print(
            f"[{F_RED}{S_BRIGHT}ERROR{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
            f"{S_RESET_ALL}]\t{S_BRIGHT}{url_error}"
        )
        print(F_BLUE + "=" * 80)

        play(path=join(base_path, "./mp3/error-call-to-attention-129258.mp3"))

        app.withdraw()
        showerror(
            title="Predictor",
            message=f"Failed to read database file.\n"
            f"Please check your internet connection...\n\n{str(url_error)}",
        )
        app.deiconify()

        return None


def update(data) -> None:
    """
    update function is used to predict, plot, and display the results
    """

    if data is None:
        return None

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Estimating Values, Please wait..."
    )

    linear_y_axis: list = []
    x_axis = data[["sl.no"]].values
    y_axis = data["price"]
    date_list = data["date"]

    min_var.set(value=min(y_axis))
    avg_var.set(value=sum(y_axis) / tot_var.get())
    max_var.set(value=max(y_axis))

    greeting_message()

    predict_linear_y_axis(linear_y_axis=linear_y_axis, x_axis=x_axis, y_axis=y_axis)

    last_val: float = list(y_axis)[-1]
    last_predicted_val: float = linear_y_axis[-1]

    accuracy_var.set(value=100)

    if last_val > last_predicted_val:
        accuracy_var.set(value=last_predicted_val / last_val * 100)

    else:
        accuracy_var.set(value=last_val / last_predicted_val * 100)

    tomorrow_var.set(value=predict(x_val=tot_var.get() + 1))
    next_week_var.set(value=predict(x_val=tot_var.get() + 7))
    next_month_var.set(value=predict(x_val=tot_var.get() + 30.4375))
    next_year_var.set(value=predict(x_val=tot_var.get() + 365.25))

    if choice.get() == 1:
        ndigits: int = 4

    if choice.get() == 2:
        ndigits: int = 2

    draw_graph(linear_y_axis=linear_y_axis, x_axis=x_axis, y_axis=y_axis, data=data)
    display_data(date_list=date_list, ndigits=ndigits)
    display_info()

    update_ui()

    return None


def update_ui() -> None:
    """
    update function is used to update the graph and data when the radio button is clicked.
    """

    for _ in ["<Control-R>", "<Control-r>"]:
        app.bind(_, lambda event: refresh())

    for _ in ["<Control-S>", "<Control-s>"]:
        app.bind(_, lambda event: dl_csv())

    for _ in ["Clear", "Refresh", "Download CSV"]:
        file_menu.entryconfig(_, state=NORMAL)

    header_lbl.configure(text=f"Hello {whoami.title()}, Welcome to Predictor")

    rb1.configure(state=NORMAL)
    rb2.configure(state=NORMAL)

    clear_btn.configure(state=NORMAL)
    refresh_btn.configure(state=NORMAL, text="Refresh")
    dl_btn.configure(state=NORMAL)
    exit_btn.configure(state=NORMAL)

    progress_value.set(value=0)
    progress_bar.configure(progress_color="#F00")
    percentage_lbl.configure(text="0.00%")

    footer_lbl.configure(
        text="Created by FOSS KINGDOM / Made with Love in Incredible India."
    )

    update_progress_bar(var=0)

    app.update()


def refresh() -> None:
    """
    refresh function is used to refresh the graph and data.
    """

    refresh_btn.configure(text="Refreshing...", state=DISABLED)
    refresh_btn.update()

    if choice.get() == 1:
        print(
            f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
            f"{S_RESET_ALL}]\t{S_BRIGHT}Refreshing, Please wait..."
        )

        usd2inr()

    if choice.get() == 2:
        print(
            f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
            f"{S_RESET_ALL}]\t{S_BRIGHT}Refreshing, Please wait..."
        )

        e_gold_24k()


def dl_csv() -> None:
    """
    download_csv function is used to download the CSV model.
    """

    for _ in ["<Control-S>", "<Control-s>"]:
        app.unbind(sequence=_)

    dl_btn.configure(state=DISABLED, text="Downloading...")
    dl_btn.update()

    try:
        if choice.get() == 1:
            content: str = get(url=USD2INR, timeout=10).content.decode(encoding="utf-8")

        if choice.get() == 2:
            content: str = get(url=E_GOLD, timeout=10).content.decode(encoding="utf-8")

        app.withdraw()
        file_location: str = asksaveasfilename(
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            defaultextension=".csv",
        )

        if file_location:
            with open(file=file_location, mode=W, encoding="utf-8") as file:
                file.write(content)
                file.close()

                print(
                    f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
                    f"{S_RESET_ALL}]\t{S_BRIGHT}CSV file downloaded successfully..."
                )
                showinfo(
                    title="Predictor", message="CSV file downloaded successfully..."
                )

        app.deiconify()

    except RequestsConnectionError as requests_connection_error:
        greeting_message()

        print(f"{S_BRIGHT}Failed to download CSV file...")
        print(f"{S_BRIGHT}Error Code: requests.exceptions.ConnectionError")
        print(
            f"[{F_RED}{S_BRIGHT}ERROR{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
            f"{S_RESET_ALL}]\t{S_BRIGHT}{requests_connection_error}"
        )
        print(F_BLUE + "=" * 80)

        play(path=join(base_path, "./mp3/error-call-to-attention-129258.mp3"))

        app.withdraw()
        showerror(
            title="Predictor",
            message=f"Failed to download CSV file...\n\n{str(requests_connection_error)}",
        )
        app.deiconify()

    for _ in ["<Control-S>", "<Control-s>"]:
        app.bind(_, lambda event: dl_csv())

    dl_btn.configure(state=NORMAL, text="Download CSV")
    dl_btn.update()


def select_all() -> None:
    """
    select_all function is used to select the entier text from the text box.
    """

    txt_box.tag_add(tagName=SEL, index1="1.0", index2=END)


def copy_to_clipboard() -> None:
    """
    copy_to_clipboard function is used to copy the text from the textbox widget.
    """

    app.clipboard_clear()

    try:
        selection: str = txt_box.selection_get()

    except TclError:
        select_all()
        selection: str = txt_box.selection_get()

    app.clipboard_append(string=selection)

    app.withdraw()
    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Successfully, copied to clipboard!!"
    )
    showinfo(title="Predictor", message="Successfully, copied to clipboard!!")
    app.deiconify()


def play(path: str) -> None:
    """
    play function is used to play the sounds and music
    """

    if sound_var.get():
        music.load(filename=path)
        music.play(loops=0)


try:
    WHITE: str = "#FFF"
    BLACK: str = "#000"
    BLUE: str = "#00F"
    RED: str = "#F00"
    ORANGE: str = "#FFA500"

    THEME_COLOR: dict = {"light": "#BCD2EE", "dark": "#242424"}

    F_GREEN: str = "\x1b[32m"
    F_BLUE: str = "\x1b[34m"
    F_RED: str = "\x1b[31m"
    F_YELLOW: str = "\x1b[33m"

    S_BRIGHT: str = "\x1b[1m"
    S_RESET_ALL: str = "\x1b[0m"

    MOUNTAIN: str = "\u26f0"
    BEATING_HEART: str = "\U0001f493"
    UP_ARROW: str = "\u2b06\ufe0f"
    DOWN_ARROW: str = "\u2b07\ufe0f"
    INFORMATION: str = "\u2139\ufe0f"

    # https://carpedm20.github.io/emoji/
    IND: str = "\U0001f1ee\U0001f1f3"
    LKA: str = "\U0001f1f1\U0001f1f0"
    SRB: str = "\U0001f1f7\U0001f1f8"
    LTU: str = "\U0001f1f1\U0001f1f9"
    EST: str = "\U0001f1ea\U0001f1ea"
    KWT: str = "\U0001f1f0\U0001f1fc"
    DOM: str = "\U0001f1e9\U0001f1f4"
    BGR: str = "\U0001f1e7\U0001f1ec"
    GHA: str = "\U0001f1ec\U0001f1ed"
    HUN: str = "\U0001f1ed\U0001f1fa"
    TUN: str = "\U0001f1f9\U0001f1f3"
    GRC: str = "\U0001f1ec\U0001f1f7"
    BGD: str = "\U0001f1e7\U0001f1e9"
    SEN: str = "\U0001f1f8\U0001f1f3"
    ZAF: str = "\U0001f1ff\U0001f1e6"
    ISR: str = "\U0001f1ee\U0001f1f1"
    NOR: str = "\U0001f1f3\U0001f1f4"
    JOR: str = "\U0001f1ef\U0001f1f4"
    GEO: str = "\U0001f1ec\U0001f1ea"
    ITA: str = "\U0001f1ee\U0001f1f9"
    DNK: str = "\U0001f1e9\U0001f1f0"
    SWE: str = "\U0001f1f8\U0001f1ea"
    PRT: str = "\U0001f1f5\U0001f1f9"
    PHL: str = "\U0001f1f5\U0001f1ed"
    ISL: str = "\U0001f1ee\U0001f1f8"
    SVN: str = "\U0001f1f8\U0001f1ee"
    DJI: str = "\U0001f1e9\U0001f1ef"
    CAN: str = "\U0001f1e8\U0001f1e6"
    USA: str = "\U0001f1fa\U0001f1f8"
    DZA: str = "\U0001f1e9\U0001f1ff"
    VEN: str = "\U0001f1fb\U0001f1ea"
    ARG: str = "\U0001f1e6\U0001f1f7"
    COL: str = "\U0001f1e8\U0001f1f4"
    BEL: str = "\U0001f1e7\U0001f1ea"
    PER: str = "\U0001f1f5\U0001f1ea"
    CHE: str = "\U0001f1e8\U0001f1ed"
    BOL: str = "\U0001f1e7\U0001f1f4"
    JAM: str = "\U0001f1ef\U0001f1f2"
    SGP: str = "\U0001f1f8\U0001f1ec"
    ECU: str = "\U0001f1ea\U0001f1e8"
    PAK: str = "\U0001f1f5\U0001f1f0"
    IDN: str = "\U0001f1ee\U0001f1e9"
    UKR: str = "\U0001f1fa\U0001f1e6"
    URY: str = "\U0001f1fa\U0001f1fe"
    MDA: str = "\U0001f1f2\U0001f1e9"
    TTO: str = "\U0001f1f9\U0001f1f9"
    UZB: str = "\U0001f1fa\U0001f1ff"
    VNM: str = "\U0001f1fb\U0001f1f3"
    BRA: str = "\U0001f1e7\U0001f1f7"
    CRI: str = "\U0001f1e8\U0001f1f7"
    SLV: str = "\U0001f1f8\U0001f1fb"
    GTM: str = "\U0001f1ec\U0001f1f9"
    HND: str = "\U0001f1ed\U0001f1f3"
    NIC: str = "\U0001f1f3\U0001f1ee"
    MEX: str = "\U0001f1f2\U0001f1fd"
    ARM: str = "\U0001f1e6\U0001f1f2"
    SAU: str = "\U0001f1f8\U0001f1e6"
    NGA: str = "\U0001f1f3\U0001f1ec"
    DEU: str = "\U0001f1e9\U0001f1ea"
    UGA: str = "\U0001f1fa\U0001f1ec"
    AZE: str = "\U0001f1e6\U0001f1ff"
    AUT: str = "\U0001f1e6\U0001f1f9"
    TUR: str = "\U0001f1f9\U0001f1f7"
    PAN: str = "\U0001f1f5\U0001f1e6"
    KHM: str = "\U0001f1f0\U0001f1ed"
    POL: str = "\U0001f1f5\U0001f1f1"
    SVK: str = "\U0001f1f8\U0001f1f0"
    OMN: str = "\U0001f1f4\U0001f1f2"
    LVA: str = "\U0001f1f1\U0001f1fb"
    LBN: str = "\U0001f1f1\U0001f1e7"
    BIH: str = "\U0001f1e7\U0001f1e6"
    ALB: str = "\U0001f1e6\U0001f1f1"
    UAE: str = "\U0001f1e6\U0001f1ea"
    FIN: str = "\U0001f1eb\U0001f1ee"
    TZA: str = "\U0001f1f9\U0001f1ff"
    KEN: str = "\U0001f1f0\U0001f1ea"
    KAZ: str = "\U0001f1f0\U0001f1ff"
    BHR: str = "\U0001f1e7\U0001f1ed"
    QAT: str = "\U0001f1f6\U0001f1e6"

    LEFT: str = "left"
    RIGHT: str = "right"
    DISABLED: str = "disabled"
    HORIZONTAL: str = "horizontal"
    BOTTOM: str = "bottom"
    X: str = "x"
    Y: str = "y"
    TOP: str = "top"
    W: str = "w"
    BOTH: str = "both"
    WORD: str = "word"
    NORMAL: str = "normal"
    END: str = "end"
    NEWS: str = "news"
    SEL: str = "sel"

    print(F_BLUE + "=" * 80 + S_RESET_ALL)

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t{S_BRIGHT}"
        f"Importing built-in libraries, Please wait...{S_RESET_ALL}"
    )

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t{S_BRIGHT}"
        f"Importing datetime, Please wait...{S_RESET_ALL}"
    )
    from datetime import datetime

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t{S_BRIGHT}"
        f"Importing getpass, Please wait...{S_RESET_ALL}"
    )
    from getpass import getuser

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t{S_BRIGHT}"
        f"Importing hashlib, Please wait...{S_RESET_ALL}"
    )
    from hashlib import sha256

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t{S_BRIGHT}"
        f"Importing os, Please wait...{S_RESET_ALL}"
    )
    from os import name
    from os import system as terminal
    from os.path import isdir, isfile, join

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t{S_BRIGHT}"
        f"Importing pathlib, Please wait...{S_RESET_ALL}"
    )
    from pathlib import Path

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t{S_BRIGHT}"
        f"Importing random, Please wait...{S_RESET_ALL}"
    )
    from random import choice

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t{S_BRIGHT}"
        f"Importing shutil, Please wait...{S_RESET_ALL}"
    )
    from shutil import rmtree

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t{S_BRIGHT}"
        f"Importing sys, Please wait...{S_RESET_ALL}"
    )
    from sys import exit as terminate

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t{S_BRIGHT}"
        f"Importing time, Please wait...{S_RESET_ALL}"
    )
    from time import strftime

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t{S_BRIGHT}"
        f"Importing tkinter, Please wait...{S_RESET_ALL}"
    )
    from tkinter import LabelFrame, Menu
    from tkinter import PhotoImage as TkPhotoImage
    from tkinter import TclError
    from tkinter.filedialog import asksaveasfilename
    from tkinter.messagebox import askyesno, showerror, showinfo
    from tkinter.ttk import Notebook

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t{S_BRIGHT}"
        f"Importing urllib, Please wait...{S_RESET_ALL}"
    )
    from urllib.error import URLError
    from urllib.request import urlopen

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t{S_BRIGHT}"
        f"Importing webbrowser, Please wait...{S_RESET_ALL}"
    )
    from webbrowser import open as browser

    whoami: str = getuser()
    today: datetime = datetime.today()
    base_path: Path = Path(__file__).parent
    uname: str = name
    __version__: str = "v.2023.06.20"

    USD2INR: str = "https://raw.githubusercontent.com/GO-FOSS/ML-Datasets/main/datasets/USD2INR.csv"
    E_GOLD: str = (
        "https://raw.githubusercontent.com/GO-FOSS/ML-Datasets/main/datasets/e-Gold.csv"
    )

    print(F_BLUE + "=" * 80 + S_RESET_ALL)

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Importing third-party modules, Please wait...{S_RESET_ALL}"
    )

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Importing colorama, Please wait...{S_RESET_ALL}"
    )
    from colorama import init as colorama_init

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Importing customtkinter, Please wait...{S_RESET_ALL}"
    )
    from customtkinter import (
        BooleanVar,
        CTk,
        CTkButton,
        CTkFrame,
        CTkImage,
        CTkLabel,
        CTkProgressBar,
        CTkRadioButton,
        CTkTextbox,
        DoubleVar,
        IntVar,
        StringVar,
        set_appearance_mode,
        set_default_color_theme,
    )

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Importing darkdetect, Please wait...{S_RESET_ALL}"
    )
    from darkdetect import isDark, isLight

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Importing matplotlib, Please wait...{S_RESET_ALL}"
    )
    from matplotlib.backends.backend_tkagg import (
        FigureCanvasTkAgg,
        NavigationToolbar2Tk,
    )
    from matplotlib.figure import Figure

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Importing pandas, Please wait...{S_RESET_ALL}"
    )
    from pandas import read_csv

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Importing pillow, Please wait...{S_RESET_ALL}"
    )
    from PIL.Image import open as img_open
    from PIL.ImageTk import PhotoImage as PILPhotoImage

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Importing psutil, Please wait...{S_RESET_ALL}"
    )
    from psutil import cpu_percent, sensors_battery, virtual_memory

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Importing pyfiglet, Please wait...{S_RESET_ALL}"
    )
    from pyfiglet import FigletFont, figlet_format

    selected_figlet_font: str = choice(FigletFont.getFonts())

    # https://www.youtube.com/watch?v=djDcVWbEYoE

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Importing pygame, Please wait...{S_RESET_ALL}"
    )
    from pygame.mixer import init as pygame_init
    from pygame.mixer import music

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Importing requests, Please wait...{S_RESET_ALL}"
    )
    from requests import get
    from requests.exceptions import ConnectionError as RequestsConnectionError

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Importing scikit-learn, Please wait...{S_RESET_ALL}"
    )
    from sklearn.linear_model import LinearRegression

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Importing termplotlib, Please wait...{S_RESET_ALL}"
    )
    from termplotlib import figure

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Importing tqdm, Please wait...{S_RESET_ALL}"
    )
    from tqdm import tqdm

    print(F_BLUE + "=" * 80 + S_RESET_ALL)

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Initializing colorama, Please wait...{S_RESET_ALL}"
    )
    colorama_init(autoreset=True)

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Initializing linear regression model, Please wait..."
    )
    model: LinearRegression = LinearRegression()

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Initializing pygame.mixer, Please wait..."
    )
    pygame_init()

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Loading GUI Application, Please wait..."
    )

    set_default_color_theme(color_string="dark-blue")

    checksum_file_path: str = join(base_path, "./checksums.txt")
    with open(file=checksum_file_path, mode="rb") as checksum_file:
        checksums = checksum_file.readlines()
        checksum_file.close()

        print(
            f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
            f"{S_RESET_ALL}]\t{S_BRIGHT}Checking hash checksums, Please wait..."
        )

        for _ in tqdm(iterable=checksums):
            _: list = _.decode().strip().split()

            check_hash(path=join(base_path, _[1]), hash_val=_[0])

    app: CTk = CTk()
    app.withdraw()

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Loading Images and Icons, Please wait..."
    )

    logo_ico_path: str = join(
        base_path,
        "./assets/0b06be6d5548392b00b646af6ae5233b12998076aefff885ba805f11dc77b38e.png",
    )
    logo_img: TkPhotoImage = TkPhotoImage(file=logo_ico_path)

    money_ico_path: str = join(
        base_path,
        "./assets/f0e3565bfd481d19f4e98ac5ebab36f58f0486ecbf17a575815fad756a0c7a0c.png",
    )
    money_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(fp=money_ico_path).resize(size=(15, 15))
    )

    gold_ico_path: str = join(
        base_path,
        "./assets/67afd30c384cb47ad3163eb9a3506af12d9afce312a32b95eba79ae65ccea069.png",
    )
    gold_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(fp=gold_ico_path).resize(size=(15, 15))
    )

    graph_ico_path: str = join(
        base_path,
        "./assets/7f83b5b8bdfc52a95db99dbcb4648fc19442117093fe4c2a181f49d70a7b173a.png",
    )
    graph_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(fp=graph_ico_path).resize(size=(15, 15))
    )

    statistic_ico_path: str = join(
        base_path,
        "./assets/c5198e617a83d22f69bb062af1ee30793af4f782b3277baba010bec2d006fc26.png",
    )
    statistic_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(fp=statistic_ico_path).resize(size=(15, 15))
    )

    info_ico_path: str = join(
        base_path,
        "./assets/be5c6fbec6b2ab5801e4eaaea8f55cae140afb4ec845794ed13c6df53b9ff1fc.png",
    )
    info_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(fp=info_ico_path).resize(size=(15, 15))
    )

    license_ico_path: str = join(
        base_path,
        "./assets/27692fb26644edb2cf919205d1ccbaccdb39121c2561967bac8bab499714883d.png",
    )
    license_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(fp=license_ico_path).resize(size=(15, 15))
    )

    video_ico_path: str = join(
        base_path,
        "./assets/3028a269eadd83a017e8f339541bea09084352df8e527f5a55483ead70469d7b.png",
    )
    video_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(fp=video_ico_path).resize(size=(15, 15))
    )

    src_ico_path: str = join(
        base_path,
        "./assets/670a4f7996dad4952cfaa567973069df03cd626aa20b6baf741bdf55925d5bac.png",
    )
    src_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(fp=src_ico_path).resize(size=(15, 15))
    )

    issues_ico_path: str = join(
        base_path,
        "./assets/79a27788b11e85d644ee833ad9776352595a3c90bd5050e76fcd3b5ff07f8ff3.png",
    )
    issues_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(fp=issues_ico_path).resize(size=(15, 15))
    )

    translation_ico_path: str = join(
        base_path,
        "./assets/3eee912f8bb42267d0ec58c6fb53fc691b32af74cf09273414250aacd987e266.png",
    )
    translation_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(fp=translation_ico_path).resize(size=(15, 15))
    )

    changelog_ico_path: str = join(
        base_path,
        "./assets/2094294042308fed55b0db58d0b5f3811eb55223779fb3025cdbd0dc0011a03a.png",
    )
    changelog_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(fp=changelog_ico_path).resize(size=(15, 15))
    )

    website_ico_path: str = join(
        base_path,
        "./assets/61f914d3e4eafd8d1b22343f2612df41fabbd469bdbf126a2bb47e092c97cd53.png",
    )
    website_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(fp=website_ico_path).resize(size=(15, 15))
    )

    email_ico_path: str = join(
        base_path,
        "./assets/b1064ea2b0f16a72a3533b0975147dd6a798fe272a51e14a72e87930833abaac.png",
    )
    email_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(fp=email_ico_path).resize(size=(15, 15))
    )

    donation_ico_path: str = join(
        base_path,
        "./assets/970f7b705f64f52597a650f953e2c61e2183d6031f55bcd0234b91a3158ac951.png",
    )
    donation_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(fp=donation_ico_path).resize(size=(15, 15))
    )

    clear_ico_light_path: str = join(
        base_path,
        "./assets/02f2216204f6969e83f72e93121c9be92b357af4b8661fc6b68444562cae9cad.png",
    )
    clear_ico_light: CTkImage = CTkImage(
        dark_image=img_open(fp=clear_ico_light_path),
        size=(15, 15),
    )

    clear_ico_dark_path: str = join(
        base_path,
        "./assets/3efda8ee324649f4ff1d6d10d12acd56effcb5c606303c023068fdb16992dbfa.png",
    )
    clear_ico_dark: PILPhotoImage = PILPhotoImage(
        image=img_open(fp=clear_ico_dark_path).resize(size=(15, 15))
    )

    refresh_ico_light_path: str = join(
        base_path,
        "./assets/0a2d117f04841eeba34613ae205c2972a69d54e55a16ddd00a855c6b2be72aa8.png",
    )
    refresh_ico_light: CTkImage = CTkImage(
        dark_image=img_open(fp=refresh_ico_light_path),
        size=(15, 15),
    )

    refresh_ico_dark: PILPhotoImage = PILPhotoImage(
        image=img_open(
            fp=join(
                base_path,
                "./assets/89a63dcbb15eb89c2b8a84d0ae9f1628f05ac09b87ea6dda72f0b59ea28219d6.png",
            )
        ).resize(size=(15, 15))
    )

    dl_ico_light: CTkImage = CTkImage(
        dark_image=img_open(
            join(
                base_path,
                "./assets/55b12d3b534b47d18a3bbd6a233d7b48301a060e02cbe4e440ca77a65f3b1653.png",
            )
        ),
        size=(15, 15),
    )

    dl_ico_dark: PILPhotoImage = PILPhotoImage(
        image=img_open(
            fp=join(
                base_path,
                "./assets/ad3693d0e1481004cbeae18a359f92182b50e64a456fd0b6e935fee4f9f2b6b0.png",
            )
        ).resize(size=(15, 15))
    )

    exit_ico_light: CTkImage = CTkImage(
        dark_image=img_open(
            fp=join(
                base_path,
                "./assets/7c209201d0eb575d5e6f733d2c5b4ec6b006437af1863682323eaafb552cfddc.png",
            )
        ),
        size=(15, 15),
    )

    exit_ico_dark: PILPhotoImage = PILPhotoImage(
        image=img_open(
            fp=join(
                base_path,
                "./assets/577d1ee752546b7a48a1b10a84e3507d93b974cdcbe7fcae599fb31c64889d93.png",
            )
        ).resize(size=(15, 15))
    )

    redirect_ico: CTkImage = CTkImage(
        dark_image=img_open(
            fp=join(
                base_path,
                "./assets/e389a5fb58d4b9286e028b615c6c0b0eb7827e0cdd9c44d6b1b066218ed696dc.png",
            )
        ),
        size=(14, 14),
    )

    google_play_ico: CTkImage = CTkImage(
        dark_image=img_open(
            fp=join(
                base_path,
                "./assets/7d4ff20320a552b5aa10c26dbdadb62e30ec2b3012f1de8ad51a80a9fe5f8463.png",
            )
        ),
        size=(15, 15),
    )

    google_ico: CTkImage = CTkImage(
        dark_image=img_open(
            fp=join(
                base_path,
                "./assets/cc30a73d1fd3653f954c3a10b6bddf22fc8958ef8aeb024d256f7e1263423724.png",
            )
        ),
        size=(80, 80),
    )

    mmtc_pamp_ico: CTkImage = CTkImage(
        dark_image=img_open(
            fp=join(
                base_path,
                "./assets/a3d98bfffd083b19d449c3315abfa6b680699c4c53f723e441984dbec7356e42.png",
            )
        ),
        size=(80, 80),
    )

    goto_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(
            fp=join(
                base_path,
                "./assets/5289ce0ccd1ad43a3f1858a692cd0b3aa99ca14934553b8406da425db4af0b87.png",
            )
        ).resize(size=(15, 15))
    )

    settings_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(
            fp=join(
                base_path,
                "./assets/56f001cc6993cb6e19e9f8717e9b95e2ac5a539d6bd2f1499898ab955558fa6f.png",
            )
        ).resize(size=(15, 15))
    )

    grid_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(
            fp=join(
                base_path,
                "./assets/04e43c35fcf86d7e94d052ce4be771ea5ce211629a7ed23a057a2d585211dc2b.png",
            )
        ).resize(size=(15, 15))
    )

    theme_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(
            fp=join(
                base_path,
                "./assets/7d56d0a5408d43bbef2fc32d6366edbb4b424935c7c83540013d2e9bb1bdd27d.png",
            )
        ).resize(size=(15, 15))
    )

    dark_theme_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(
            fp=join(
                base_path,
                "./assets/d5514c42954896f52e92f4dc1b576930f00d2dab5ee81354074b653bce3949c2.png",
            )
        ).resize(size=(15, 15))
    )

    light_theme_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(
            fp=join(
                base_path,
                "./assets/0556f0067a04d547ffa6484164c334bebcad53a656fc538cf45b7e5e3e72361d.png",
            )
        ).resize(size=(15, 15))
    )

    sys_theme_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(
            fp=join(
                base_path,
                "./assets/a0c743cc7f9227b9c7dc3cd35ed1e6f6d96f6c3e99ce2f6f5f0bdb988c480bf5.png",
            )
        ).resize(size=(15, 15))
    )

    speaker_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(
            fp=join(
                base_path,
                "./assets/89c9a89bcd9f123e6113f12c8e21e3130ab46caffa832cfa910de5f6f9882844.png",
            )
        ).resize(size=(15, 15))
    )

    copy_ico_path: str = join(
        base_path,
        "./assets/2f554adc4f02d5165cd3d7c3934529223a38b3fb78bf8e6c979e958833a5eb2f.png",
    )
    copy_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(fp=copy_ico_path).resize(size=(15, 15))
    )

    print(F_BLUE + "=" * 80)

    greeting_message()

    app.title(string=f"Predictor {__version__}")
    set_title()

    app.maxsize(width=app.winfo_screenwidth(), height=app.winfo_screenheight())
    app.resizable(width=False, height=False)
    app.iconphoto(True, logo_img)

    for _ in ["Q", "q", "<Escape>"]:
        app.bind(_, lambda event: exit_app())

    menu_bar: Menu = Menu(master=app)

    app.configure(menu=menu_bar)

    # File Menu
    file_menu: Menu = Menu(master=menu_bar, tearoff=False)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open", accelerator="(Ctrl+O)")
    predict_menu: Menu = Menu(master=file_menu, tearoff=False)
    file_menu.add_cascade(label="Predict", menu=predict_menu)
    predict_menu.add_command(
        label="USD/INR rate", image=money_ico, compound=LEFT, command=usd2inr
    )
    predict_menu.add_command(
        label="24K e-Gold", image=gold_ico, compound=LEFT, command=e_gold_24k
    )
    predict_menu.add_separator()
    predict_menu.add_command(label="Custom")
    goto_menu: Menu = Menu(master=file_menu, tearoff=False)
    file_menu.add_cascade(label="Goto", compound=LEFT, menu=goto_menu, image=goto_ico)
    goto_menu.add_command(
        label="Graph",
        image=graph_ico,
        compound=LEFT,
        accelerator="(Alt+1)",
        command=lambda: tab_view.select(tab_id=0),
    )
    goto_menu.add_command(
        label="Data",
        image=statistic_ico,
        compound=LEFT,
        accelerator="(Alt+2)",
        command=lambda: tab_view.select(tab_id=1),
    )
    goto_menu.add_command(
        label="Info",
        image=info_ico,
        compound=LEFT,
        accelerator="(Alt+3)",
        command=lambda: tab_view.select(tab_id=2),
    )
    preferences_menu: Menu = Menu(master=app, tearoff=False)
    file_menu.add_cascade(
        label="Preferences", compound=LEFT, menu=preferences_menu, image=settings_ico
    )

    grid_var: IntVar = IntVar(master=app, value=3)
    grid_menu: Menu = Menu(master=preferences_menu, tearoff=False)
    preferences_menu.add_cascade(
        label="Toggle grid lines", compound=LEFT, menu=grid_menu, image=grid_ico
    )
    grid_menu.add_radiobutton(
        label="Show grid lines (Horizontal)",
        value=1,
        variable=grid_var,
        command=toggle_grid_lines,
    )
    grid_menu.add_radiobutton(
        label="Show grid lines (Vertical)",
        value=2,
        variable=grid_var,
        command=toggle_grid_lines,
    )
    grid_menu.add_radiobutton(
        label="Show grid lines (Both)",
        value=3,
        variable=grid_var,
        command=toggle_grid_lines,
    )
    grid_menu.add_radiobutton(
        label="Hide grid lines", value=4, variable=grid_var, command=toggle_grid_lines
    )
    theme_var: IntVar = IntVar(master=app, value=3)
    themes_menu: Menu = Menu(master=preferences_menu, tearoff=False)
    preferences_menu.add_cascade(
        label="Theme preference", compound=LEFT, menu=themes_menu, image=theme_ico
    )
    themes_menu.add_radiobutton(
        label="Dark Theme",
        compound=LEFT,
        image=dark_theme_ico,
        value=1,
        variable=theme_var,
        command=configure_theme_color,
    )
    themes_menu.add_radiobutton(
        label="Light Theme",
        compound=LEFT,
        image=light_theme_ico,
        value=2,
        variable=theme_var,
        command=configure_theme_color,
    )
    themes_menu.add_radiobutton(
        label="System Default",
        compound=LEFT,
        image=sys_theme_ico,
        value=3,
        variable=theme_var,
        command=configure_theme_color,
    )
    sound_var: BooleanVar = BooleanVar(master=app, value=True)
    preferences_menu.add_checkbutton(
        label="Play sounds",
        compound=RIGHT,
        image=speaker_ico,
        onvalue=True,
        offvalue=False,
        variable=sound_var,
    )
    file_menu.add_separator()
    file_menu.add_command(
        label="Clear",
        compound=LEFT,
        state=DISABLED,
        command=reset_ui,
        image=clear_ico_dark,
    )
    file_menu.add_command(
        label="Refresh",
        accelerator="(Ctrl+R)",
        compound=LEFT,
        state=DISABLED,
        command=refresh,
        image=refresh_ico_dark,
    )
    file_menu.add_command(
        label="Download CSV",
        accelerator="(Ctrl+S)",
        compound=LEFT,
        state=DISABLED,
        command=dl_csv,
        image=dl_ico_dark,
    )
    file_menu.add_separator()
    file_menu.add_command(
        label="Exit",
        accelerator="(Ctrl+Q)",
        compound=LEFT,
        command=exit_app,
        image=exit_ico_dark,
    )

    # Links Menu
    links_menu: Menu = Menu(master=menu_bar, tearoff=False)
    menu_bar.add_cascade(label="Links", menu=links_menu)
    links_menu.add_command(label="License (GPL-v3.0)", image=license_ico, compound=LEFT)
    links_menu.add_command(label="Video (YouTube)", image=video_ico, compound=LEFT)
    links_menu.add_command(label="Source Code (GitHub)", image=src_ico, compound=LEFT)
    links_menu.add_command(label="Issues", image=issues_ico, compound=LEFT)
    links_menu.add_command(label="Translation", image=translation_ico, compound=LEFT)
    links_menu.add_command(label="Changelog", image=changelog_ico, compound=LEFT)
    links_menu.add_command(label="Website", image=website_ico, compound=LEFT)
    links_menu.add_command(label="E-Mail Author", image=email_ico, compound=LEFT)

    # Help Menu
    help_menu: Menu = Menu(master=menu_bar, tearoff=False)
    menu_bar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(
        label="About Predictor",
        accelerator=f"({INFORMATION})",
        image=info_ico,
        compound=LEFT,
        command=lambda: browser(url="https://github.com/JahidFariz/Predictor#readme"),
    )
    help_menu.add_separator()
    help_menu.add_command(
        label="Make a donation",
        accelerator="($)",
        command=lambda: browser(url="https://paypal.me/jahidfariz"),
        image=donation_ico,
        compound=LEFT,
    )

    header_lbl: CTkLabel = CTkLabel(
        master=app,
        text=f"Hello {whoami.title()}, Welcome to Predictor",
        fg_color=BLACK,
        text_color=WHITE,
    )
    header_lbl.pack(side=TOP, fill=X)

    month: int = today.month
    day: int = today.day

    if month == 1:
        if day == 1:
            special_day_banner(msg="New Year's Day")

        if day == 26:
            special_day_banner(msg=f"India {IND} Republic Day")

    if month == 2:
        if day == 4:
            special_day_banner(msg=f"Sri Lanka {LKA} Independence Day")

        if day == 6:
            special_day_banner(msg="Waitangi Day")

        if day == 14:
            special_day_banner(msg=f"Valentine's Day {BEATING_HEART}")

        if day == 15:
            special_day_banner(msg=f"Serbia {SRB} National Day")

        if day == 16:
            special_day_banner(msg=f"Lithuania {LTU} Independence Day")

        if day == 24:
            special_day_banner(msg=f"Estonia {EST} Independence Day")

        if day == 25:
            special_day_banner(msg=f"Kuwait {KWT} National Day")

        if day == 27:
            special_day_banner(msg=f"Dominican Republic {DOM} Independence Day")

    if month == 3:
        if day == 1:
            special_day_banner(msg="St. David's Day")

        if day == 3:
            special_day_banner(msg=f"Bulgaria {BGR} Liberation Day")

        if day == 6:
            special_day_banner(msg=f"Ghana {GHA} Independence Day")

        if day == 8:
            special_day_banner(msg="International Women's Day")

        if day == 15:
            special_day_banner(msg=f"Hungary {HUN} National Day")

        if day == 20:
            special_day_banner(msg=f"Tunisia {TUN} National Day")

        if day == 25:
            special_day_banner(msg=f"Greece {GRC} National Day")

        if day == 26:
            special_day_banner(msg=f"Bangladesh {BGD} Independence Day")

    if month == 4:
        if day == 4:
            special_day_banner(msg=f"Senegal {SEN} Independence Day")

        if day == 22:
            special_day_banner(msg="Earth Day")

        if day == 23:
            day_list: list = [
                "National Sovereignty and Children's Day",
                "St. George's Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if day == 27:
            day_list: list = [
                "King's Day",
                f"South Africa {ZAF} Freedom Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

    if month == 5:
        if day == 5:
            special_day_banner(msg=f"Israel {ISR} Independence Day")

        if day == 17:
            special_day_banner(msg=f"Norway {NOR} Constitution Day")

        if day == 25:
            special_day_banner(msg=f"Jordan {JOR} Independence Day")

        if day == 26:
            special_day_banner(msg=f"Georgia {GEO} Independence Day")

    if month == 6:
        if day == 2:
            day_list: list = ["World Environment Day", f"Italy {ITA} Republic Day"]
            special_day_banner(msg=choice(seq=day_list))

        if day == 5:
            special_day_banner(msg=f"Denmark {DNK} Constitution Day")

        if day == 6:
            special_day_banner(msg=f"Sweden {SWE} National Day")

        if day == 10:
            special_day_banner(msg=f"Portugal {PRT} National Day")

        if day == 12:
            special_day_banner(msg=f"Philippines {PHL} Independence Day")

        if day == 17:
            special_day_banner(msg=f"Iceland {ISL} National Day")

        if day == 25:
            special_day_banner(msg=f"Slovenia {SVN} National Day")

        if day == 27:
            special_day_banner(msg=f"Djibouti {DJI} Independence Day")

    if month == 7:
        if day == 1:
            special_day_banner(msg=f"Canada {CAN} Day")

        if day == 4:
            special_day_banner(msg=f"Fourth of July USA {USA}")

        if day == 5:
            day_list: list = [
                f"Algeria {DZA} Independence Day",
                f"Venezuela {VEN} Independence Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if day == 9:
            special_day_banner(msg=f"Argentina {ARG} Independence Day")

        if day == 14:
            special_day_banner(msg="Bastille Day")

        if day == 20:
            special_day_banner(msg=f"Colombia {COL} Independence Day")

        if day == 21:
            special_day_banner(msg=f"Belgium {BEL} National Day")

        if day == 28:
            special_day_banner(msg=f"Peru {PER} Independence Day")

    if month == 8:
        if day == 1:
            special_day_banner(msg=f"Switzerland {CHE} National Day")

        if day == 6:
            day_list: list = [
                f"Bolivia {BOL} Independence Day",
                f"Jamaica {JAM} Independence Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if day == 9:
            special_day_banner(msg=f"Singapore {SGP} National Day")

        if day == 10:
            special_day_banner(msg=f"Ecuador {ECU} Independence Day")

        if day == 11:
            special_day_banner(msg=f"Mountain {MOUNTAIN} Day")

        if day == 14:
            special_day_banner(msg=f"Pakistan {PAK} Independence Day")

        if day == 15:
            day_list: list = [
                "National Liberation Day of Korea",
                f"India {IND} Independence Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if day == 17:
            special_day_banner(msg=f"Indonesia {IDN} Independence Day")

        if day == 24:
            special_day_banner(msg=f"Ukraine {UKR} Independence Day")

        if day == 25:
            special_day_banner(msg=f"Uruguay {URY} Independence Day")

        if day == 27:
            special_day_banner(msg=f"Republic of Moldova {MDA} Independence Day")

        if day == 31:
            day_list: list = [
                "Hari Merdeka",
                f"Trinidad & Tobago {TTO} Independence Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

    if month == 9:
        if day == 1:
            special_day_banner(msg=f"Uzbekistan {UZB} Independence Day")

        if day == 2:
            special_day_banner(msg=f"Vietnam {VNM} National Day")

        if day == 7:
            special_day_banner(msg=f"Brazil {BRA} Independence Day")

        if day == 15:
            day_list: list = [
                f"Costa Rica {CRI} Independence Day",
                f"El Salvador {SLV} Independence Day",
                f"Guatemala {GTM} Independence Day",
                f"Honduras {HND} National Day",
                f"Nicaragua {NIC} Independence Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if day == 16:
            special_day_banner(msg=f"Mexico {MEX} Independence Day")

        if day == 19:
            special_day_banner(msg="Respect for the Aged Day")

        if day == 21:
            special_day_banner(msg=f"Armenia {ARM} Independence Day")

        if day == 23:
            special_day_banner(msg=f"Saudi Arabia {SAU} National Day")

    if month == 10:
        if day == 1:
            special_day_banner(msg=f"Nigeria {NGA} Independence Day")

        if day == 3:
            special_day_banner(msg=f"German {DEU} Unity Day")

        if day == 9:
            day_list: list = ["Hangul Day", f"Uganda {UGA} Independence Day"]
            special_day_banner(msg=choice(seq=day_list))

        if day == 18:
            special_day_banner(msg=f"Azerbaijan {AZE} Independence Day")

        if day == 26:
            special_day_banner(msg=f"Austria {AUT} National Day")

        if day == 29:
            special_day_banner(msg=f"Turkey {TUR} National Day")

    if month == 11:
        if day == 3:
            special_day_banner(msg=f"Panama {PAN} Independence Day")

        if day == 9:
            special_day_banner(msg=f"Cambodia {KHM} Independence Day")

        if day == 11:
            day_list: list = [f"Poland {POL} National Day", "Veterans Day"]
            special_day_banner(msg=choice(seq=day_list))

        if day == 17:
            day_list: list = [
                "Czech Republic Freedom and Democracy Day",
                f"Slovakia {SVK} Freedom and Democracy Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if day == 18:
            day_list: list = [
                f"Oman {OMN} National Day",
                f"Latvia {LVA} Independence Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if day == 22:
            special_day_banner(msg=f"Lebanon {LBN} Independence Day")

        if day == 25:
            special_day_banner(msg=f"Bosnia & Herzegovina {BIH} Statehood Day")

        if day == 28:
            special_day_banner(msg=f"Albania {ALB} Independence Day")

        if day == 30:
            special_day_banner(msg="St. Andrew's Day")

    if month == 12:
        if day == 1:
            special_day_banner(msg="Great Union Day")

        if day == 2:
            special_day_banner(msg=f"UAE {UAE} National Day")

        if day == 6:
            special_day_banner(msg=f"Finland {FIN} Independence Day")

        if day == 9:
            special_day_banner(msg=f"Tanzania {TZA} Independence Day")

        if day == 12:
            special_day_banner(msg=f"Kenya {KEN} Independence Day")

        if day == 16:
            day_list: list = [
                f"Kazakhstan {KAZ} Independence Day",
                f"Bahrain {BHR} National Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if day == 18:
            special_day_banner(msg=f"Qatar {QAT} National Day")

        if day == 31:
            special_day_banner(msg="New Year's Eve")

    lbl_frame_1: LabelFrame = LabelFrame(
        master=app,
        text="What would you like to predict?",
        fg=RED,
    )
    lbl_frame_1.pack(fill=X, padx=10, ipadx=5, ipady=5)

    choice: IntVar = IntVar(master=app, value=0)

    rb1: CTkRadioButton = CTkRadioButton(
        master=lbl_frame_1,
        text="USD/INR Exchange Rates",
        variable=choice,
        value=1,
        command=usd2inr,
    )
    rb1.pack(padx=10, side=LEFT)

    rb2: CTkRadioButton = CTkRadioButton(
        master=lbl_frame_1,
        text="24K e-Gold Price by MMTC-PAMP",
        variable=choice,
        value=2,
        command=e_gold_24k,
    )
    rb2.pack(padx=10, side=LEFT)

    btn_frame_1: CTkFrame = CTkFrame(master=app)
    btn_frame_1.pack(ipady=5, padx=10)

    clear_btn: CTkButton = CTkButton(
        master=btn_frame_1,
        text="Clear",
        image=clear_ico_light,
        compound=LEFT,
        width=120,
        command=reset_ui,
        state=DISABLED,
    )
    clear_btn.pack(padx=5, side=LEFT)

    refresh_btn: CTkButton = CTkButton(
        master=btn_frame_1,
        text="Refresh",
        image=refresh_ico_light,
        compound=LEFT,
        width=120,
        command=refresh,
        state=DISABLED,
    )
    refresh_btn.pack(padx=5, side=LEFT)

    dl_btn: CTkButton = CTkButton(
        master=btn_frame_1,
        text="Download CSV",
        image=dl_ico_light,
        compound=LEFT,
        width=120,
        command=dl_csv,
        state=DISABLED,
    )
    dl_btn.pack(padx=5, side=LEFT)

    exit_btn: CTkButton = CTkButton(
        master=btn_frame_1,
        text="Exit",
        image=exit_ico_light,
        compound=LEFT,
        width=120,
        command=exit_app,
        fg_color=RED,
    )
    exit_btn.pack(padx=5, side=LEFT)

    tab_view: Notebook = Notebook(master=app)
    tab_view.pack(fill=BOTH, expand=True)

    graph_frame: CTkFrame = CTkFrame(master=tab_view)
    graph_frame.pack()

    data_frame: CTkFrame = CTkFrame(master=tab_view)
    data_frame.pack()

    info_frame: CTkFrame = CTkFrame(master=tab_view)
    info_frame.pack()

    tab_view.add(child=graph_frame, text="Graph", image=graph_ico, compound=LEFT)
    tab_view.add(child=data_frame, text="Data", image=statistic_ico, compound=LEFT)
    tab_view.add(child=info_frame, text="Info", image=info_ico, compound=LEFT)

    app.bind("<Alt-KeyPress-1>", lambda event: tab_view.select(tab_id=0))
    app.bind("<Alt-KeyPress-2>", lambda event: tab_view.select(tab_id=1))
    app.bind("<Alt-KeyPress-3>", lambda event: tab_view.select(tab_id=2))

    fig: Figure = Figure()

    graph_title_var: StringVar = StringVar(master=app, value="Graph Area")
    x_label_var: StringVar = StringVar(master=app, value="X-Axis")
    y_label_var: StringVar = StringVar(master=app, value="Y-Axis")

    graph_text_color: StringVar = StringVar(master=app, value=BLACK)

    set_graph_labels()

    graph = fig.add_subplot()

    canvas: FigureCanvasTkAgg = FigureCanvasTkAgg(fig, master=graph_frame)
    toolbar: NavigationToolbar2Tk = NavigationToolbar2Tk(canvas, graph_frame)
    toolbar.pack()
    fig.canvas.draw()
    canvas.get_tk_widget().pack(fill=BOTH, expand=True)

    CTkLabel(
        master=data_frame, text="* The formula for Linear Regression is (y = mx + b)"
    ).pack()

    lbl_frame_2: LabelFrame = LabelFrame(
        master=data_frame, text="Statistic Data", fg=RED
    )
    lbl_frame_2.pack(padx=10, fill=BOTH)

    tot_var: IntVar = IntVar(master=app, value=0)
    CTkLabel(master=lbl_frame_2, text="Total Records (n):").grid(
        row=0, column=0, padx=10, sticky=W
    )
    tot_data_lbl: CTkLabel = CTkLabel(master=lbl_frame_2, text=tot_var.get(), width=180)
    tot_data_lbl.grid(row=0, column=1, padx=10, sticky=NEWS)

    min_var: DoubleVar = DoubleVar(master=app, value=0)
    CTkLabel(master=lbl_frame_2, text="Minimum:").grid(
        row=1, column=0, padx=10, sticky=W
    )
    min_val_lbl: CTkLabel = CTkLabel(master=lbl_frame_2, text=min_var.get(), width=180)
    min_val_lbl.grid(row=1, column=1, padx=10, sticky=NEWS)

    avg_var: DoubleVar = DoubleVar(master=app, value=0)
    CTkLabel(master=lbl_frame_2, text="Average:").grid(
        row=2, column=0, padx=10, sticky=W
    )
    avg_val_lbl: CTkLabel = CTkLabel(master=lbl_frame_2, text=avg_var.get(), width=180)
    avg_val_lbl.grid(row=2, column=1, padx=10, sticky=NEWS)

    max_var: DoubleVar = DoubleVar(master=app, value=0)
    CTkLabel(master=lbl_frame_2, text="Maximum:").grid(
        row=3, column=0, padx=10, sticky=W
    )
    max_val_lbl: CTkLabel = CTkLabel(master=lbl_frame_2, text=max_var.get(), width=180)
    max_val_lbl.grid(row=3, column=1, padx=10, sticky=NEWS)

    coef_var: DoubleVar = DoubleVar(master=app, value=0)
    CTkLabel(master=lbl_frame_2, text="Coefficient (m):").grid(
        row=4, column=0, padx=10, sticky=W
    )
    coef_lbl: CTkLabel = CTkLabel(master=lbl_frame_2, text=coef_var.get(), width=180)
    coef_lbl.grid(row=4, column=1, padx=10, sticky=NEWS)

    intercept_var: DoubleVar = DoubleVar(master=app, value=0)
    CTkLabel(master=lbl_frame_2, text="Intercept (b):").grid(
        row=5, column=0, padx=10, sticky=W
    )
    intercept_lbl: CTkLabel = CTkLabel(
        master=lbl_frame_2, text=intercept_var.get(), width=180
    )
    intercept_lbl.grid(row=5, column=1, padx=10, sticky=NEWS)

    accuracy_var: DoubleVar = DoubleVar(master=app, value=0)
    CTkLabel(master=lbl_frame_2, text="Accuracy:").grid(
        row=6, column=0, padx=10, sticky=W
    )
    accuracy_lbl: CTkLabel = CTkLabel(
        master=lbl_frame_2, text=f"{accuracy_var.get()}%", width=180
    )
    accuracy_lbl.grid(row=6, column=1, padx=10, sticky=NEWS)

    tomorrow_var: DoubleVar = DoubleVar(master=app, value=0)
    CTkLabel(master=lbl_frame_2, text="Tomorrow expected:").grid(
        row=7, column=0, padx=10, sticky=W
    )
    tomorrow_lbl: CTkLabel = CTkLabel(
        master=lbl_frame_2,
        text=tomorrow_var.get(),
        fg_color=BLUE,
        text_color=WHITE,
        width=180,
        corner_radius=10,
    )
    tomorrow_lbl.grid(row=7, column=1, padx=10, sticky=NEWS)

    next_week_var: DoubleVar = DoubleVar(master=app, value=0)
    CTkLabel(master=lbl_frame_2, text="Next week expected:").grid(
        row=8, column=0, padx=10, sticky=W
    )
    next_week_lbl: CTkLabel = CTkLabel(
        master=lbl_frame_2,
        text=next_week_var.get(),
        fg_color=ORANGE,
        text_color=WHITE,
        width=180,
        corner_radius=10,
    )
    next_week_lbl.grid(row=8, column=1, padx=10, sticky=NEWS)

    next_month_var: DoubleVar = DoubleVar(master=app, value=0)
    CTkLabel(master=lbl_frame_2, text="Next month expected:").grid(
        row=9, column=0, padx=10, sticky=W
    )
    next_month_lbl: CTkLabel = CTkLabel(
        master=lbl_frame_2,
        text=next_month_var.get(),
        fg_color="green",
        text_color=WHITE,
        width=180,
        corner_radius=10,
    )
    next_month_lbl.grid(row=9, column=1, padx=10, sticky=NEWS)

    next_year_var: DoubleVar = DoubleVar(master=app, value=0)
    CTkLabel(master=lbl_frame_2, text="Next year expected:").grid(
        row=10, column=0, padx=10, sticky=W
    )
    next_year_lbl: CTkLabel = CTkLabel(
        master=lbl_frame_2,
        text=next_year_var.get(),
        fg_color=RED,
        text_color=WHITE,
        width=180,
        corner_radius=10,
    )
    next_year_lbl.grid(row=10, column=1, padx=10, sticky=NEWS)

    CTkLabel(master=lbl_frame_2, text="Status:").grid(
        row=11, column=0, padx=10, sticky=W
    )
    stat_lbl: CTkLabel = CTkLabel(
        master=lbl_frame_2, text="N/A", text_color="purple", width=180
    )
    stat_lbl.grid(row=11, column=1, padx=10, sticky=NEWS)

    CTkLabel(master=lbl_frame_2, text="Last updated:").grid(
        row=12, column=0, padx=10, sticky=W
    )
    last_update_lbl: CTkLabel = CTkLabel(master=lbl_frame_2, text="N/A", width=180)
    last_update_lbl.grid(row=12, column=1, padx=10, sticky=NEWS)

    btn_frame_2: CTkFrame = CTkFrame(master=data_frame)
    btn_frame_2.pack(ipady=5)

    src_btn: CTkButton = CTkButton(
        master=btn_frame_2,
        text="Source",
        image=redirect_ico,
        compound=LEFT,
        width=110,
        state=DISABLED,
    )
    src_btn.pack(padx=5, side=LEFT)

    google_play_btn: CTkButton = CTkButton(
        master=btn_frame_2,
        text="Google Play",
        image=google_play_ico,
        compound=LEFT,
        width=110,
        state=DISABLED,
    )
    google_play_btn.pack(padx=5, side=LEFT)

    lbl_frame_3: LabelFrame = LabelFrame(master=data_frame, text="Powered by", fg=RED)
    lbl_frame_3.pack(padx=10, ipady=5, pady=(0, 5), fill=BOTH, expand=True)

    CTkLabel(master=lbl_frame_3, image=google_ico, text=None).grid(
        row=0, column=0, padx=5
    )
    CTkLabel(master=lbl_frame_3, image=mmtc_pamp_ico, text=None).grid(
        row=0, column=1, padx=5
    )

    txt_box: CTkTextbox = CTkTextbox(master=info_frame, wrap=WORD, corner_radius=25)
    txt_box.insert(index="1.0", text=f"No information available ({INFORMATION})...")
    txt_box.configure(state=DISABLED)
    txt_box.pack(fill=BOTH, expand=True, padx=10, pady=10)

    # https://www.youtube.com/watch?v=KRuUtNxOb_k&t=466s
    popup_menu: Menu = Menu(master=txt_box, tearoff=False)
    popup_menu.add_command(
        label="Select All", accelerator="(Ctrl+A)", command=select_all
    )
    popup_menu.add_command(
        label="Copy",
        compound=LEFT,
        accelerator="(Ctrl+C)",
        image=copy_ico,
        command=copy_to_clipboard,
    )

    footer_lbl: CTkLabel = CTkLabel(
        master=app,
        text=f"Created by FOSS Kingdom / Made with Love {BEATING_HEART} in Incredible India {IND}",
        fg_color=BLACK,
        text_color=WHITE,
    )
    footer_lbl.pack(side=BOTTOM, fill=X)

    stat_frame: CTkFrame = CTkFrame(master=app)
    stat_frame.pack(side=BOTTOM, fill=X, ipady=5)

    cpu_lbl: CTkLabel = CTkLabel(
        master=stat_frame,
        corner_radius=10,
        text="CPU: 0.00%",
        fg_color="#0F0",
        text_color=BLACK,
    )
    cpu_lbl.pack(side=LEFT, ipadx=5, padx=(5, 0))
    cpu_stat()

    mem_lbl: CTkLabel = CTkLabel(
        master=stat_frame,
        corner_radius=10,
        text="MEM: 0.00%",
        fg_color="#0F0",
        text_color=BLACK,
    )
    mem_lbl.pack(side=LEFT, ipadx=5, padx=(5, 0))
    mem_stat()

    pwr_lbl: CTkLabel = CTkLabel(
        master=stat_frame,
        corner_radius=10,
        text="PWR: 0.00%",
        fg_color="#F00",
        text_color=BLACK,
    )
    pwr_lbl.pack(side=LEFT, ipadx=5, padx=(5, 5))
    pwr_stat()

    time_lbl: CTkLabel = CTkLabel(
        master=stat_frame, text=f"{whoami.title()} @ 00:00:00"
    )
    time_lbl.pack(side=RIGHT, padx=10)
    time_stat()

    progress_frame: CTkFrame = CTkFrame(master=app)
    progress_frame.pack(fill=X, side=BOTTOM)

    CTkLabel(master=progress_frame, text="Job:").pack(padx=(10, 5), side=LEFT)

    progress_value: DoubleVar = DoubleVar(master=app, value=0)
    progress_bar: CTkProgressBar = CTkProgressBar(
        master=progress_frame,
        orientation=HORIZONTAL,
        variable=progress_value,
        progress_color="#F00",
    )
    progress_bar.pack(fill=X, expand=True, padx=5, side=LEFT)

    percentage_lbl: CTkLabel = CTkLabel(master=progress_frame, text="0.00%", width=45)
    percentage_lbl.pack(padx=(5, 10), side=LEFT)

    toggle_grid_lines()
    configure_theme_color()

    app.deiconify()

    play(path=join(base_path, "./mp3/click-124467.mp3"))

    app.mainloop()

except TclError as tcl_error:
    greeting_message()

    print(S_BRIGHT + "Error Code: tkinter.TclError")
    print(
        f"[{F_RED}{S_BRIGHT}ERROR{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}{S_RESET_ALL}]"
        f"\t{S_BRIGHT}{tcl_error}"
    )
    print(F_BLUE + "=" * 80)

    clr_cache()

    print(F_GREEN + S_BRIGHT + "Bye!!")

    terminate()

except ModuleNotFoundError as module_not_found_error:
    clrscr()

    print("=" * 80)
    print("Error Code: builtins.ModuleNotFoundError")
    print(f"[ERROR]\t[{datetime.now()}]\t{module_not_found_error}")
    print("=" * 80)

    clr_cache()

    print("Bye!!")

    terminate()
