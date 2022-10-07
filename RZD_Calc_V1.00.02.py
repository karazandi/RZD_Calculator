import webbrowser
from tkinter import *
from PIL import ImageTk, Image
import math

import customtkinter

customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root=customtkinter.CTk()
root.title("RZD Calculator Project")
root.geometry("900x650")
root.resizable(False, False)

#Function Definition
def contact_wa():
    webbrowser.open_new(url="https://wa.me/6287874965587")

def contact_email():
    webbrowser.open_new(url="mailto:karazandi@gmail.com")

def back():
    root.geometry("600x150")
    rc_calc_frame.pack_forget()
    rc_calc_result.pack_forget()
    supp_calc_frame.pack_forget()
    supp_calc_result.pack_forget()
    supp_backbutton.pack_forget()
    rc_backbutton.pack_forget()
    supp_desc_frame.pack_forget()
    rc_desc_frame.pack_forget()
    calc_opt_click.set(" ")
    calc_select.pack(padx=10, pady=10)

    #value reset
    code_click.set(" ")
    lc_click.set(" ")
    class_click.set(" ")
    nps_click.set(" ")
    excoat_click.set(" ")
    incoat_click.set(" ")
    insul_click.set(" ")
    def_input.set(" ")
    rc_soil_click.set(" ")
    rc_pavement_click.set(" ")
    rc_contactarea_click.set(" ")
    rc_axleload_click.set(" ")
    rc_code_click.set(" ")
    rc_lc_click.set(" ")
    rc_class_click.set(" ")
    rc_nps_click.set(" ")
    thickness_entry.delete(0, END)
    excoat_thk_entry.delete(0, END)
    excoat_dens_entry.delete(0, END)
    incoat_thk_entry.delete(0, END)
    incoat_dens_entry.delete(0, END)
    insul_thk_entry.delete(0, END)
    insul_dens_entry.delete(0, END)
    def_entry.delete(0, END)
    rc_thickness_entry.delete(0, END)
    rc_excoat_thk_entry.delete(0, END)
    rc_maop_entry.delete(0, END)
    rc_maot_entry.delete(0, END)
    rc_ambtemp_entry.delete(0, END)
    rc_soilunit_entry.delete(0, END)
    rc_soilreaction_entry.delete(0, END)
    rc_resilientsoil_entry.delete(0, END)
    rc_contactarea_entry.delete(0, END)
    rc_axleload_entry.delete(0, END)
    rc_burial_entry.delete(0, END)

def calculator_start():
    sel_calc = str(calc_opt_click.get())
    if sel_calc == "Onshore Pipe Support Spacing Calculator":
        root.geometry("600x900")
        calc_select.pack_forget()
        supp_calc_def.pack_forget()
        rc_calc_def.pack_forget()
        supp_backbutton.pack(side=BOTTOM)
        supp_calc_frame.pack(side=TOP, padx=10, pady=10)

    if sel_calc == "Onshore Pipeline Road Crossing Calculator":
        root.geometry("800x800")
        calc_select.pack_forget()
        supp_calc_def.pack_forget()
        rc_calc_def.pack_forget()
        rc_backbutton.pack(side=BOTTOM)
        rc_calc_frame.pack(padx=10, pady=10, side=LEFT, anchor="n")

def calc_opt_sel(sel_calc):
    sel_calc=str(calc_opt_click.get())
    if sel_calc=="Onshore Pipe Support Spacing Calculator":
        root.geometry("900x800")
        rc_calc_def.pack_forget()
        supp_desc_frame.pack(padx=10, pady=10)
        supp_calc_def.pack()
    if sel_calc=="Onshore Pipeline Road Crossing Calculator":
        root.geometry("800x700")
        supp_calc_def.pack_forget()
        rc_desc_frame.pack(padx=10, pady=10)
        rc_calc_def.pack()

def begin():
    welcome.pack_forget()
    root.geometry("600x150")
    calc_select.pack(padx=10, pady=10)
    calc_opt_frame.pack(padx=10, pady=10)
    calc_opt_drop.grid(row=0, column=0, padx=10, pady=10)
    start_calc.grid(row=0, column=1, padx=10, pady=10)

def code_sel(sel_code):
    sel_code=code_click.get()
    global des_fac
    code=str(sel_code)
    if code=="ASME B31.4":
        lc_label.grid_remove()
        lc_drop.grid_remove()
        des_fac = float(0.72)
    if code=="ASME B31.8":
        lc_label.grid(row=1, column=0, pady=2)
        lc_drop.grid(row=1, column=1, columnspan=2, pady=2)

def rc_code_sel(rc_sel_code):
    rc_sel_code=rc_code_click.get()
    global rc_des_fac
    rc_code=str(rc_sel_code)
    if rc_code=="ASME B31.4":
        rc_lc_label.grid_remove()
        rc_lc_drop.grid_remove()
        rc_des_fac = float(0.72)
    if rc_code=="ASME B31.8":
        rc_lc_label.grid(row=1, column=0, pady=2)
        rc_lc_drop.grid(row=1, column=1, columnspan=2, pady=2)

def lc_sel(sel_lc):
    sel_lc=lc_click.get()
    lc=str(sel_lc)
    global des_fac
    if lc=="Location Class 1, Div. 1":
        des_fac=float(0.8)
    if lc=="Location Class 1, Div. 2":
        des_fac=float(0.72)
    if lc=="Location Class 2":
        des_fac=float(0.6)
    if lc=="Location Class 3":
        des_fac=float(0.5)
    if lc=="Location Class 4":
        des_fac=float(0.4)

def rc_lc_sel(rc_sel_lc):
    rc_sel_lc=rc_lc_click.get()
    rc_lc=str(rc_sel_lc)
    global rc_des_fac
    if rc_lc=="Location Class 1, Div. 1":
        rc_des_fac=float(0.8)
    if rc_lc=="Location Class 1, Div. 2":
        rc_des_fac=float(0.72)
    if rc_lc=="Location Class 2":
        rc_des_fac=float(0.6)
    if rc_lc=="Location Class 3":
        rc_des_fac=float(0.5)
    if rc_lc=="Location Class 4":
        rc_des_fac=float(0.4)

def class_sel(sel_class):
    sel_class=class_click.get()
    matclass=str(sel_class)
    global smys
    if matclass=="API 5L Gr. A":
        smys=float(30000*6894.76)
    if matclass=="API 5L Gr. B":
        smys=float(35000*6894.76)
    if matclass=="API 5L X42":
        smys=float(42000*6894.76)
    if matclass=="API 5L X46":
        smys=float(46000*6894.76)
    if matclass=="API 5L X52":
        smys=float(52000*6894.76)
    if matclass=="API 5L X56":
        smys=float(56000*6894.76)
    if matclass=="API 5L X60":
        smys=float(60000*6894.76)
    if matclass=="API 5L X65":
        smys=float(65000*6894.76)
    if matclass=="API 5L X70":
        smys=float(70000*6894.76)
    if matclass=="API 5L X80":
        smys=float(80000*6894.76)

def rc_class_sel(rc_sel_class):
    rc_sel_class=rc_class_click.get()
    rc_matclass=str(rc_sel_class)
    global rc_smys
    if rc_matclass=="API 5L Gr. A":
        rc_smys=float(30000*6894.76)
    if rc_matclass=="API 5L Gr. B":
        rc_smys=float(35000*6894.76)
    if rc_matclass=="API 5L X42":
        rc_smys=float(42000*6894.76)
    if rc_matclass=="API 5L X46":
        rc_smys=float(46000*6894.76)
    if rc_matclass=="API 5L X52":
        rc_smys=float(52000*6894.76)
    if rc_matclass=="API 5L X56":
        rc_smys=float(56000*6894.76)
    if rc_matclass=="API 5L X60":
        rc_smys=float(60000*6894.76)
    if rc_matclass=="API 5L X65":
        rc_smys=float(65000*6894.76)
    if rc_matclass=="API 5L X70":
        rc_smys=float(70000*6894.76)
    if rc_matclass=="API 5L X80":
        rc_smys=float(80000*6894.76)

def nps_sel(sel_nps):
    sel_nps=nps_click.get()
    nps=str(sel_nps)
    global od
    if nps=="1/8":
        od=float(10.3/1000)
    if nps=="1/4":
        od=float(13.7/1000)
    if nps=="1 1/4":
        od=float(17.1/1000)
    if nps=="1/2":
        od=float(21.3/1000)
    if nps=="13/4":
        od=float(26.7/1000)
    if nps=="1":
        od=float(33.4/1000)
    if nps=="1 1/4":
        od=float(42.2/1000)
    if nps=="1 1/2":
        od=float(48.3/1000)
    if nps=="2":
        od=float(60.3/1000)
    if nps=="2 1/2":
        od=float(73/1000)
    if nps=="3":
        od=float(88.9/1000)
    if nps=="4":
        od=float(114.3/1000)
    if nps=="5":
        od=float(141.3/1000)
    if nps=="6":
        od=float(168.3/1000)
    if nps=="8":
        od=float(219.1/1000)
    if nps=="10":
        od=float(273/1000)
    if nps=="12":
        od=float(323.8/1000)
    if nps=="14":
        od=float(355.6/1000)
    if nps=="16":
        od=float(406.4/1000)
    if nps=="18":
        od=float(457/1000)
    if nps=="20":
        od=float(508/1000)
    if nps=="22":
        od=float(559/1000)
    if nps=="24":
        od=float(610/1000)
    if nps=="26":
        od=float(610/1000)
    if nps=="28":
        od=float(711/1000)
    if nps=="30":
        od=float(762/1000)
    if nps=="32":
        od=float(813/1000)
    if nps=="34":
        od=float(864/1000)
    if nps=="36":
        od=float(914/1000)
    if nps=="38":
        od=float(965/1000)
    if nps=="40":
        od=float(1016/1000)
    if nps=="42":
        od=float(1067/1000)
    if nps=="44":
        od=float(1118/1000)
    if nps=="46":
        od=float(1168/1000)
    if nps=="48":
        od=float(1219/1000)
    if nps=="52":
        od=float(1321/1000)
    if nps=="56":
        od=float(1422/1000)
    if nps=="60":
        od=float(1524/1000)
    if nps=="64":
        od=float(1626/1000)
    if nps=="68":
        od=float(1727/1000)
    if nps=="72":
        od=float(1829/1000)
    if nps=="76":
        od=float(1930/1000)
    if nps=="80":
        od=float(2032/1000)

def rc_nps_sel(rc_sel_nps):
    rc_sel_nps=rc_nps_click.get()
    rc_nps=str(rc_sel_nps)
    global rc_od
    if rc_nps=="1/8":
        rc_od=float(10.3/1000)
    if rc_nps=="1/4":
        rc_od=float(13.7/1000)
    if rc_nps=="1 1/4":
        rc_od=float(17.1/1000)
    if rc_nps=="1/2":
        rc_od=float(21.3/1000)
    if rc_nps=="13/4":
        rc_od=float(26.7/1000)
    if rc_nps=="1":
        rc_od=float(33.4/1000)
    if rc_nps=="1 1/4":
        rc_od=float(42.2/1000)
    if rc_nps=="1 1/2":
        rc_od=float(48.3/1000)
    if rc_nps=="2":
        rc_od=float(60.3/1000)
    if rc_nps=="2 1/2":
        rc_od=float(73/1000)
    if rc_nps=="3":
        rc_od=float(88.9/1000)
    if rc_nps=="4":
        rc_od=float(114.3/1000)
    if rc_nps=="5":
        rc_od=float(141.3/1000)
    if rc_nps=="6":
        rc_od=float(168.3/1000)
    if rc_nps=="8":
        rc_od=float(219.1/1000)
    if rc_nps=="10":
        rc_od=float(273/1000)
    if rc_nps=="12":
        rc_od=float(323.8/1000)
    if rc_nps=="14":
        rc_od=float(355.6/1000)
    if rc_nps=="16":
        rc_od=float(406.4/1000)
    if rc_nps=="18":
        rc_od=float(457/1000)
    if rc_nps=="20":
        rc_od=float(508/1000)
    if rc_nps=="22":
        rc_od=float(559/1000)
    if rc_nps=="24":
        rc_od=float(610/1000)
    if rc_nps=="26":
        rc_od=float(610/1000)
    if rc_nps=="28":
        rc_od=float(711/1000)
    if rc_nps=="30":
        rc_od=float(762/1000)
    if rc_nps=="32":
        rc_od=float(813/1000)
    if rc_nps=="34":
        rc_od=float(864/1000)
    if rc_nps=="36":
        rc_od=float(914/1000)
    if rc_nps=="38":
        rc_od=float(965/1000)
    if rc_nps=="40":
        rc_od=float(1016/1000)
    if rc_nps=="42":
        rc_od=float(1067/1000)
    if rc_nps=="44":
        rc_od=float(1118/1000)
    if rc_nps=="46":
        rc_od=float(1168/1000)
    if rc_nps=="48":
        rc_od=float(1219/1000)
    if rc_nps=="52":
        rc_od=float(1321/1000)
    if rc_nps=="56":
        rc_od=float(1422/1000)
    if rc_nps=="60":
        rc_od=float(1524/1000)
    if rc_nps=="64":
        rc_od=float(1626/1000)
    if rc_nps=="68":
        rc_od=float(1727/1000)
    if rc_nps=="72":
        rc_od=float(1829/1000)
    if rc_nps=="76":
        rc_od=float(1930/1000)
    if rc_nps=="80":
        rc_od=float(2032/1000)

def excoat_sel(sel_excoat):
    sel_excoat=excoat_click.get()
    global excoat
    excoat=str(sel_excoat)
    global thicknessexcoat
    global density_excoat
    if excoat=="no":
        excoat_thk_label.grid_remove()
        excoat_density_label.grid_remove()
        excoat_thk_entry.grid_remove()
        excoat_dens_entry.grid_remove()
        thicknessexcoat=float(0)
    if excoat=="yes":
        excoat_thk_label.grid(row=7, column=0, pady=2)
        excoat_density_label.grid(row=8, column=0, pady=2)
        excoat_thk_entry.grid(row=7, column=1, columnspan=2, pady=2)
        excoat_dens_entry.grid(row=8, column=1, columnspan=2, pady=2)

def incoat_sel(sel_incoat):
    sel_incoat=incoat_click.get()
    global incoat
    incoat=str(sel_incoat)
    global thicknessincoat
    global density_incoat
    if incoat=="no":
        incoat_thk_label.grid_remove()
        incoat_density_label.grid_remove()
        incoat_thk_entry.grid_remove()
        incoat_dens_entry.grid_remove()
        thicknessincoat=float(0)
    if incoat=="yes":
        incoat_thk_label.grid(row=13, column=0, pady=2)
        incoat_density_label.grid(row=14, column=0, pady=2)
        incoat_thk_entry.grid(row=13, column=1, columnspan=2, pady=2)
        incoat_dens_entry.grid(row=14, column=1, columnspan=2, pady=2)

def insul_sel(sel_insul):
    sel_insul=insul_click.get()
    global insul
    insul=str(sel_insul)
    global thicknessinsul
    global density_insul
    if insul=="no":
        insul_thk_label.grid_remove()
        insul_density_label.grid_remove()
        insul_thk_entry.grid_remove()
        insul_dens_entry.grid_remove()
        thicknessinsul=float(0)
    if insul=="yes":
        insul_thk_label.grid(row=10, column=0, pady=2)
        insul_density_label.grid(row=11, column=0, pady=2)
        insul_thk_entry.grid(row=10, column=1, columnspan=2, pady=2)
        insul_dens_entry.grid(row=11, column=1, columnspan=2, pady=2)

def soil_sel(sel_soil):
    sel_soil=str(rc_soil_click.get())

def pavement_sel(sel_pavement):
    sel_pavement=str(rc_pavement_click.get())

def contactarea_sel(sel_contactarea):
    sel_contactarea=str(rc_contactarea_click.get())
    global contactareaofwheel
    if sel_contactarea == "API Standard":
        rc_contactarea_entry.grid_remove()
        rc_contactareainput_label.grid_remove()
        contactareaofwheel = float(0.092903)
    if sel_contactarea == "User Defined":
        rc_contactareainput_label.grid(row=16, column=0, pady=2)
        rc_contactarea_entry.grid(row=16, column=1, columnspan=2, pady=2)

def axleload_sel(sel_axleload):
    sel_axleload=str(rc_axleload_click.get())
    global axleload_selected
    axleload_selected=sel_axleload
    if sel_axleload == "User Defined":
        rc_axleloadinput_label.grid(row=18, column=0, pady=2)
        rc_axleload_entry.grid(row=18, column=1, columnspan=2, pady=2)
    if sel_axleload == "API Standard":
        rc_axleload_entry.grid_remove()
        rc_axleloadinput_label.grid_remove()

def sub_calc():
    supp_calc_result.pack(padx=10, pady=10)
    if excoat =="no":
        thicknessexcoat=float(0)
        density_excoat =float(0)
    if excoat == "yes":
        thicknessexcoat = excoat_thk_entry.get()
        density_excoat = excoat_dens_entry.get()
    if incoat =="no":
        thicknessincoat=float(0)
        density_incoat =float(0)
    if incoat == "yes":
        thicknessincoat = incoat_thk_entry.get()
        density_incoat = incoat_dens_entry.get()
    if insul =="no":
        thicknessinsul=float(0)
        density_insul =float(0)
    if insul == "yes":
        thicknessinsul = insul_thk_entry.get()
        density_insul = insul_dens_entry.get()
    steel_density = float(7850)
    steel_modulus = float(207000000000)
    water_density=float(1000)
    pipethickness=float(thickness_entry.get())/1000
    deflection=float(def_entry.get())/1000

    ODexcoat=od+(2*float(thicknessexcoat)/1000)
    ODinsul=ODexcoat+(2*float(thicknessinsul)/1000)
    IDpipe=od-(2*float(pipethickness))
    IDincoat=IDpipe-(2*float(thicknessincoat)/1000)

    od2=od**2
    od4=od**4
    ODexcoat2=ODexcoat**2
    ODinsul2=ODinsul**2
    IDpipe2=IDpipe**2
    IDpipe4=IDpipe**4
    IDincoat2=IDincoat**2
    piA=math.pi/4
    piI=math.pi/64
    piZ=math.pi/(32*od)

    Apipe=piA*(od2-IDpipe2)
    Aexcoat=piA*(ODexcoat2-od2)
    Ainsul=piA*(ODinsul2-ODexcoat2)
    Aincoat=piA*(IDpipe2-IDincoat2)
    Aint=piA*IDincoat2

    Ipipe=piI*(od4-IDpipe4)
    Zpipe=piZ*(od4-IDpipe4)

    wemp=((Apipe*steel_density)+(Aexcoat*float(density_excoat))+(Ainsul*float(density_insul))+(Aincoat*float(density_incoat)))*9.81
    wfill=((Apipe*steel_density)+(Aexcoat*float(density_excoat))+(Ainsul*float(density_insul))+(Aincoat*float(density_incoat))+(Aint*water_density))*9.81

    deltaempty=(float(deflection)*384*steel_modulus*Ipipe)/(5*wemp)
    eldeltaempty=deltaempty**(0.25)

    deltafilled=(float(deflection)*384*steel_modulus*Ipipe)/(5*wfill)
    eldeltafilled=deltafilled**(0.25)

    slsempty=(des_fac*smys*Zpipe)/(wemp)
    elslsempty=slsempty**(0.5)

    slsfilled = (des_fac*smys * Zpipe) / (wfill)
    elslsfilled = slsfilled ** (0.5)

    ulsempty= (smys*Zpipe)/wemp
    elulsempty=ulsempty**(0.5)

    ulsfilled = (smys * Zpipe) / wfill
    elulsfilled = ulsfilled ** (0.5)

    def_result_empty = customtkinter.CTkLabel(supp_calc_result, text=str(round(eldeltaempty,3)) + " m")
    def_result_filled = customtkinter.CTkLabel(supp_calc_result, text=str(round(eldeltafilled,3)) + " m")

    sls_result_empty = customtkinter.CTkLabel(supp_calc_result, text=str(round(elslsempty,3)) + " m")
    sls_result_filled = customtkinter.CTkLabel(supp_calc_result, text=str(round(elslsfilled,3)) + " m")

    uls_result_empty = customtkinter.CTkLabel(supp_calc_result, text=str(round(elulsempty,3)) + " m")
    uls_result_filled = customtkinter.CTkLabel(supp_calc_result, text=str(round(elulsfilled,3)) + " m")

    def_result_empty.grid(row=20, column=1, pady=2)
    def_result_filled.grid(row=20, column=2, pady=2)

    sls_result_empty.grid(row=21, column=1, pady=2)
    sls_result_filled.grid(row=21, column=2, pady=2)

    uls_result_empty.grid(row=22, column=1, pady=2)
    uls_result_filled.grid(row=22, column=2, pady=2)


    pipe_condition_label = customtkinter.CTkLabel(supp_calc_result, text="Pipe Condition", borderwidth=1).grid(row=18, column=1, columnspan=2, pady=2)
    max_span_label = customtkinter.CTkLabel(supp_calc_result, text="Maximum Support Spacing", borderwidth=1).grid(row=18, column=0, rowspan=2, pady=2)
    empty_label = customtkinter.CTkLabel(supp_calc_result, text="Empty", borderwidth=1).grid(row=19, column=1, pady=2)
    filled_label = customtkinter.CTkLabel(supp_calc_result, text="Filled with Water", borderwidth=1).grid(row=19, column=2, pady=2)

    result_def_label = customtkinter.CTkLabel(supp_calc_result, text="Deflection Limited: ").grid(row=20, column=0, pady=2)
    result_sls_label = customtkinter.CTkLabel(supp_calc_result, text="Serviceability Limit State: ").grid(row=21, column=0, pady=2)
    result_uls_label = customtkinter.CTkLabel(supp_calc_result, text="Ultimate Limit State: ").grid(row=22, column=0, pady=2)

def rc_calc():
    root.geometry("1200x700")
    rc_calc_result.pack(padx=10, pady=10, side=RIGHT, anchor="n")

    rc_nps = int(rc_nps_click.get())
    thermalexpansioncoeff=float(0.0000117)
    poissonratio=float(0.3)
    vonmisesfactor=float(0.9)
    burialdepth=int(rc_burial_entry.get())
    burialarea=(burialdepth * rc_od)+((rc_od**2) / 2)-(0.5 * math.pi * ((rc_od**2) / 4))
    steel_modulus = float(207000000000)

    maop=int(rc_maop_entry.get()) * 6894.76
    pipethickness=float(rc_thickness_entry.get())/1000

    optemp=float(rc_maot_entry.get())
    ambtemp=float(rc_ambtemp_entry.get())

    barlowstress_=((maop * rc_od) / (2 * pipethickness)) / 1000000
    barlowstress =round(barlowstress_,3)

    soilunitweight=float(rc_soilunit_entry.get()) * 1000

    thicknessexcoat=int(rc_excoat_thk_entry.get())
    ODexcoat = rc_od + (2 * float(thicknessexcoat) / 1000)
    boreddiameter = ODexcoat + float(0.58)

    barlowint_= ((maop * (rc_od - pipethickness)) / (2 * pipethickness)) / 1000000
    barlowint=round(barlowint_,3)

    allowablestress_=(rc_smys * rc_des_fac) / 1000000
    allowablestress=round(allowablestress_,3)

    if barlowstress < allowablestress:
        barlowunitycheck="SAFE"
    if barlowstress > allowablestress:
        barlowunitycheck="FAIL"

    rc_barlowunitycheck_result = customtkinter.CTkLabel(rc_calc_result, text=barlowunitycheck)

    #circumferential stress due to earth load
    wtodratio=pipethickness / rc_od
    depthtoboreratio=burialdepth / burialarea
    boredtopiperatio=burialarea / rc_od

    modulussoilreaction_input=float(rc_soilreaction_entry.get())
    modulussoilreaction=modulussoilreaction_input * 689475.72931783
    if modulussoilreaction_input==0.2:
        khex=(2100092861658 * ((pipethickness / rc_od)**6)) - (614950413729 * ((pipethickness / rc_od)**5)) + (73056624256 * ((pipethickness / rc_od)**4)) - (4540511514 * (((pipethickness / rc_od)**3))) + (158347132 * (((pipethickness / rc_od)**2))) - (3044452 * (pipethickness / rc_od)) + 27293
    if modulussoilreaction_input==0.5:
        khex=(int(-647943474385) * ((pipethickness / rc_od)**6)) + (168620357420 * ((pipethickness / rc_od)**5)) - (16066442894 * ((pipethickness / rc_od)**4)) + (607829414 * (((pipethickness / rc_od)**3))) - (308617 * (((pipethickness / rc_od)**2))) - (569637 * (pipethickness / rc_od)) + 11814
    if modulussoilreaction_input==1:
        khex=(233206840207 * ((pipethickness / rc_od)**6)) - (62088102640 * ((pipethickness / rc_od)**5)) + (6920592127 * ((pipethickness / rc_od)**4)) - (449099075 * (((pipethickness / rc_od)**3))) + (19823819 * (((pipethickness / rc_od)**2))) - (588562 * (pipethickness / rc_od)) + 9168
    if modulussoilreaction_input==2:
        khex=(1015486155462 * ((pipethickness / rc_od)**6)) - (277630552096 * ((pipethickness / rc_od)**5)) + (30009633092 * ((pipethickness / rc_od)**4)) - (1642394636 * (((pipethickness / rc_od)**3))) + (49049259 * (((pipethickness / rc_od)**2))) - (49049259 * (pipethickness / rc_od)) + 8461

    khe=khex

    soiltype=str(rc_soil_click.get())
    if soiltype=="Loose to medium dense sands and gravels; soft clays and silts":
        bex=(int(-0.000000056189911) * ((burialdepth / boreddiameter)**6)) + (0.000005828370305 * ((burialdepth / boreddiameter)**5)) - (0.000242999058272 * ((burialdepth / boreddiameter)**4)) + (0.005272406945927 * (((burialdepth / boreddiameter)**3))) - (0.064568995158142 * (((burialdepth / boreddiameter)**2))) + (0.443628700839310 * (burialdepth / boreddiameter)) - 0.038657590628526
    if soiltype=="Dense to very dense sands and gravels; medium to very stiff clays and silts":
        bex = (int(-0.000000064839688) * ((burialdepth / boreddiameter) ** 6)) + (0.000006707899115 * ((burialdepth / boreddiameter) ** 5)) - (0.000276878607022 * ((burialdepth / boreddiameter) ** 4)) + (0.005859977314610 * (((burialdepth / boreddiameter) ** 3))) - (0.068155604250811 * (((burialdepth / boreddiameter) ** 2))) + (0.428233860453387 * (burialdepth / boreddiameter)) - 0.030499092276006

    be=bex

    eex1=(0.300588353013154 * ((boreddiameter / rc_od)**6)) - (1.243101952862790 * ((boreddiameter / rc_od)**5)) + (1.965251642548410 * ((boreddiameter / rc_od)**4)) - (1.457862820600290 * ((boreddiameter / rc_od)**3)) + (0.630545967009443 * ((boreddiameter / rc_od)**2)) +(0.778127183722660 * (boreddiameter / rc_od)) + 0.073824120628835
    if eex1 > 1.4:
        eex=1.4
    if eex1 <= 1.4:
        eex=eex1

    ee=eex

    circumstressearthload_=(khe * be * ee * soilunitweight * ODexcoat) / 1000000
    circumstressearthload=round(circumstressearthload_,3)

    #Impact Factor
    if burialdepth <= 1.5:
        impactfactor=1.5
    if burialdepth > 1.5 and burialdepth < 6.5:
        impactfactor=1.5 - (burialdepth - 1.5) * 0.1
    if burialdepth >= 6.5:
        impactfactor=1

    #Critical Axle Configuration and Load
    pavementtype=str(rc_pavement_click.get())

    if burialdepth < 1.2 and int(rc_nps) <= 12 and pavementtype=="No Pavement":
        axleconfig="Single Axle"
    else:
        axleconfig="Tandem Axle"

    if axleconfig=="Single Axle" and axleload_selected=="API Standard":
        axleload=53400
    if axleconfig=="Tandem Axle" and axleload_selected=="API Standard":
        axleload=44500
    if axleload_selected=="User Defined":
        axleload=int(rc_axleload_entry.get()) * 1000

    contactarea=str(rc_contactarea_click.get())
    if contactarea == "API Standard":
        contactareaofwheel=144 * 0.00064516
    if contactarea == "User Defined":
        contactareaofwheel=int(rc_contactarea_entry.get())

    applieddesignsurfacepressure_=(axleload / contactareaofwheel)
    applieddesignsurfacepressure=round(applieddesignsurfacepressure_,3)

    if pavementtype == "Flexible Pavement":
        rf1=1
        rf2=1
    if pavementtype == "Rigid Pavement":
        rf1=0.9
        rf2=0.9
    if pavementtype == "No Pavement" and axleconfig == "Single Axle":
        rf1=1.2
    if pavementtype == "No Pavement" and axleconfig == "Tandem Axle":
        rf1=1.1
    if pavementtype == "No Pavement":
        rf2=1.1

    if burialdepth < 1.2 and int(rc_nps) <= 12:
        rf=rf1
    else:
        rf=rf2

    #Cyclic Circumferential Stress
    if axleconfig == "Tandem Axle":
        lf1=1
        lf2=1
    if axleconfig == "Single Axle":
        lf2=0.65
    if pavementtype == "Flexible Pavement" and axleconfig == "Single Axle":
        lf1=0.75
    if pavementtype == "No Pavement" and axleconfig == "Single Axle":
        lf1=0.8
    if pavementtype == "Rigid Pavement" and axleconfig == "Single Axle":
        lf1=0.65

    if burialdepth < 1.2 and int(rc_nps) <= 12:
        lf=lf1
    else:
        lf=lf2

    resilientmodulus_input=float(rc_resilientsoil_entry.get())
    resilientmodulus=resilientmodulus_input * 689475.72931783
    if resilientmodulus_input == 5:
        khhx = (int(-2531212703.26562) * ((pipethickness / rc_od) ** 6)) + (887231698.93448 * ((pipethickness / rc_od) ** 5)) - (124295518.13994 * ((pipethickness / rc_od) ** 4)) + (8790604.91004 * (((pipethickness / rc_od) ** 3))) - (320797.33117 * (((pipethickness / rc_od) ** 2))) + (5117.01903 * (pipethickness / rc_od)) - 7.74208
    if resilientmodulus_input == 10:
        khhx = (int(-4063337180.72656) * ((pipethickness / rc_od) ** 6)) + (1238789763.52141 * ((pipethickness / rc_od) ** 5)) - (151849046.82691 * ((pipethickness / rc_od) ** 4)) + (9511896.13031 * (((pipethickness / rc_od) ** 3))) - (315704.17964 * (((pipethickness / rc_od) ** 2))) + (4878.28289 * (pipethickness / rc_od)) - 12.73716
    if resilientmodulus_input == 20:
        khhx = (int(-898744511.94141) * ((pipethickness / rc_od) ** 6)) + (313999364.25977 * ((pipethickness / rc_od) ** 5)) - (44637362.47231 * ((pipethickness / rc_od) ** 4)) + (3298634.79153 * (((pipethickness / rc_od) ** 3))) - (132048.64519 * (((pipethickness / rc_od) ** 2))) + (2505.78006 * (pipethickness / rc_od)) - 7.94077

    khh=khhx

    gh1=(int(-0.0000000000000000262722239) * (rc_od**6)) + (0.0000000000001005255516953 * (rc_od**5)) - (0.0000000001503939327393190 * (rc_od**4)) + (0.0000001100362310903900000 * (rc_od**3)) - (0.0000395817833736911000000 * (rc_od**2)) + (0.0054190777118198200000000 * (rc_od)) + 1.2349479556901400000000000
    gh2=(int(-0.0000000000000000156142539) * (rc_od**6)) + (0.0000000000000601730243176 * (rc_od**5)) - (0.0000000000914872473097034 * (rc_od**4)) + (0.0000000691860909773271000 * (rc_od**3)) - (0.0000265188313358345000000 * (rc_od**2)) + (0.0040446021487866300000000 * (rc_od)) + 0.9408099361381870000000000
    gh3=(int(-0.0000000000000000053724401) * (rc_od**6)) + (0.0000000000000222144725803 * (rc_od**5)) - (0.0000000000365983173809189 * (rc_od**4)) + (0.0000000303133788899035000 * (rc_od**3)) - (0.0000129344005579986000000 * (rc_od**2)) + (0.0022140788610923800000000 * (rc_od)) + 0.7610446705946120000000000
    gh4=(int(-0.0000000000000000056466981) * (rc_od**6)) + (0.0000000000000233031151422 * (rc_od**5)) - (0.0000000000378358565804342 * (rc_od**4)) + (0.0000000305244553920591000 * (rc_od**3)) - (0.0000125710049406901000000 * (rc_od**2)) + (0.0021057077112473200000000 * (rc_od)) + 0.5936359422893890000000000
    gh5=gh2 - (((1.8 - burialdepth) / 0.6) * (gh2 - gh1))
    gh6=gh3 - (((2.4 - burialdepth) / 0.6) * (gh3 - gh2))
    gh7=gh4 - (((3 - burialdepth) / 0.6) * (gh4 - gh3))

    if burialdepth >= 0.9 and burialdepth <= 1.2:
        ghx=gh1
    if burialdepth == 1.8:
        ghx=gh2
    if burialdepth == 2.4:
        ghx=gh3
    if burialdepth == 3:
        ghx=gh4
    if burialdepth > 1.2 and burialdepth < 1.8:
        ghx=gh5
    if burialdepth > 1.8 and burialdepth < 2.4:
        ghx=gh6
    if burialdepth > 2.4 and burialdepth < 3:
        ghx=gh7

    ghh=ghx

    cycliccircumferentialstress_=(khh * ghh * rf * lf * impactfactor * applieddesignsurfacepressure) / 1000000
    cycliccircumferentialstress=round(cycliccircumferentialstress_,3)

    #Cyclic Longitudinal Stress
    if resilientmodulus_input == 5:
        klhx = (int(-1232472433.62500) * ((pipethickness / rc_od) ** 6)) + (416261796.62187 * ((pipethickness / rc_od) ** 5)) - (56468358.22371 * ((pipethickness / rc_od) ** 4)) + (3893511.49262 * (((pipethickness / rc_od) ** 3))) - (139432.97614 * (((pipethickness / rc_od) ** 2))) + (2185.36153 * (pipethickness / rc_od)) + 3.02931
    if resilientmodulus_input == 10:
        klhx = (152198452.57031 * ((pipethickness / rc_od) ** 6)) - (15004444.53910 * ((pipethickness / rc_od) ** 5)) - (2984113.26128 * ((pipethickness / rc_od) ** 4)) + (556744.79117 * (((pipethickness / rc_od) ** 3))) - (31912.50546 * (((pipethickness / rc_od) ** 2))) + (613.97940 * (pipethickness / rc_od)) + 6.21460
    if resilientmodulus_input == 20:
        klhx = (int(-275800272.50000) * ((pipethickness / rc_od) ** 6)) + (97489560.62998 * ((pipethickness / rc_od) ** 5)) - (14156890.42469 * ((pipethickness / rc_od) ** 4)) + (1080957.46765 * (((pipethickness / rc_od) ** 3))) - (44497.27609 * (((pipethickness / rc_od) ** 2))) + (822.85274 * (pipethickness / rc_od)) + 1.20309

    klh=klhx

    glh1 = (0.0000000000000000585991986 * (rc_od ** 6)) - (0.0000000000002237205154298 * (rc_od ** 5)) + (0.0000000003428730227009360 * (rc_od ** 4)) - (0.0000002699276150250640000 * (rc_od ** 3)) + (0.0001153629230989520000000 * (rc_od ** 2)) - (0.0259843828469761000000000 * (rc_od)) + 3.5902674381287900000000000
    glh2 = (0.0000000000000000837853442 * (rc_od ** 6)) - (0.0000000000003107437976057 * (rc_od ** 5)) + (0.0000000004604027132245390 * (rc_od ** 4)) - (0.0000003485342273496820000 * (rc_od ** 3)) + (0.0001425937367235610000000 * (rc_od ** 2)) - (0.0306335666777532000000000 * (rc_od)) + 3.7692808125567500000000000
    glh3 = (0.0000000000000000880359199 * (rc_od ** 6)) - (0.0000000000003270058722557 * (rc_od ** 5)) + (0.0000000004851487468136570 * (rc_od ** 4)) - (0.0000003676616216496810000 * (rc_od ** 3)) + (0.0001506544770908360000000 * (rc_od ** 2)) - (0.0324634482928872000000000 * (rc_od)) + 3.8368199056234800000000000
    glh4 = (0.0000000000000001011457212 * (rc_od ** 6)) - (0.0000000000003741640713643 * (rc_od ** 5)) + (0.0000000005507244868145560 * (rc_od ** 4)) - (0.0000004116463385443470000 * (rc_od ** 3)) + (0.0001651945977571210000000 * (rc_od ** 2)) - (0.0346697472772093000000000 * (rc_od)) + 3.8586164402567400000000000
    glh5 = glh2 - (((1.8 - burialdepth) / 0.6) * (glh2 - glh1))
    glh6 = glh3 - (((2.4 - burialdepth) / 0.6) * (glh3 - glh2))
    glh7 = glh4 - (((3 - burialdepth) / 0.6) * (glh4 - glh3))

    if burialdepth >= 0.9 and burialdepth <= 1.2:
        glhx = glh1
    if burialdepth == 1.8:
        glhx = glh2
    if burialdepth == 2.4:
        glhx = glh3
    if burialdepth == 3:
        glhx = glh4
    if burialdepth > 1.2 and burialdepth < 1.8:
        glhx = glh5
    if burialdepth > 1.8 and burialdepth < 2.4:
        glhx = glh6
    if burialdepth > 2.4 and burialdepth < 3:
        glhx = glh7

    glh = glhx

    cycliclongitudinalstress_= (klh * glh * rf *lf *impactfactor * applieddesignsurfacepressure) / 1000000
    cycliclongitudinalstress=round(cycliclongitudinalstress_,3)

    maxcircumferentialstress_=(circumstressearthload + cycliccircumferentialstress + barlowstress)
    maxcircumferentialstress=round(maxcircumferentialstress_,3)
    maxlongitudinalstress_=(cycliclongitudinalstress - ((thermalexpansioncoeff * steel_modulus * (optemp - ambtemp)) / 1000000) + (poissonratio * (circumstressearthload + barlowstress)))
    maxlongitudinalstress=round(maxlongitudinalstress_,3)
    maxradialstress_=(int(-maop))  / 1000000
    maxradialstress=round(maxradialstress_,3)
    effectivestress_=(((0.5 * (((maxcircumferentialstress - maxlongitudinalstress)**2))) + ((maxlongitudinalstress - maxradialstress)**2) + ((maxradialstress - maxcircumferentialstress)**2))**0.5)
    effectivestress=round(effectivestress_,3)

    if effectivestress < allowablestress:
        effectivestress_unitycheck="SAFE"
    if effectivestress > allowablestress:
        effectivestress_unitycheck="FAIL"

    rc_effectivestress_unitycheck = customtkinter.CTkLabel(rc_calc_result, text=effectivestress_unitycheck)

    girthlimit_=((12000*6894.76) * rc_des_fac) /1000000
    girthlimit=round(girthlimit_,3)
    longlimit_=((23000*6894.76) * rc_des_fac) /1000000
    longlimit=round(longlimit_,3)

    rc_girthallow=customtkinter.CTkLabel(rc_calc_result, text=str(girthlimit)+ " MPa")
    rc_longallow = customtkinter.CTkLabel(rc_calc_result, text=str(longlimit)+ " MPa")

    if cycliclongitudinalstress <= girthlimit:
        girthunitycheck="SAFE"
    if cycliclongitudinalstress > girthlimit:
        girthunitycheck="FAIL"

    if cycliclongitudinalstress <= longlimit:
        longunitycheck="SAFE"
    if cycliclongitudinalstress > longlimit:
        longunitycheck="FAIL"

    rc_girthunitycheck = customtkinter.CTkLabel(rc_calc_result, text=girthunitycheck)
    rc_longunitycheck = customtkinter.CTkLabel(rc_calc_result, text=longunitycheck)

    rc_allowablestress_result=customtkinter.CTkLabel(rc_calc_result, text=str(allowablestress)+ " MPa").grid(row=0, column=1, columnspan=2, pady=2)
    rc_barlowstress_result=customtkinter.CTkLabel(rc_calc_result, text=str(barlowstress)+ " MPa").grid(row=1, column=1, columnspan=2, pady=2)
    rc_barlowunitycheck_result.grid(row=2, column=1, columnspan=2, pady=2)
    rc_circuminternalstress_result = customtkinter.CTkLabel(rc_calc_result, text=str(barlowint)+ " MPa").grid(row=3, column=1, columnspan=2, pady=2)
    rc_circumstress_result = customtkinter.CTkLabel(rc_calc_result,text=str(circumstressearthload)+ " MPa").grid(row=4,column=1,columnspan=2,pady=2)
    rc_surfaceload_result = customtkinter.CTkLabel(rc_calc_result,text=str(round((applieddesignsurfacepressure_/1000000),3))+ " MPa").grid(row=5,column=1,columnspan=2,pady=2)
    rc_impactfactor_result = customtkinter.CTkLabel(rc_calc_result,text=str(impactfactor)).grid(row=6,column=1,columnspan=2, pady=2)
    rc_cycliccircumstress_result = customtkinter.CTkLabel(rc_calc_result,text=str(cycliccircumferentialstress)+ " MPa").grid(row=7,column=1,columnspan=2,pady=2)
    rc_cycliclongstress_result = customtkinter.CTkLabel(rc_calc_result,text=str(cycliclongitudinalstress)+ " MPa").grid(row=8,column=1,columnspan=2,pady=2)
    rc_maxcircumstress_result = customtkinter.CTkLabel(rc_calc_result, text=str(maxcircumferentialstress)+ " MPa").grid(row=9,column=1,columnspan=2,pady=2)
    rc_maxlongstress_result = customtkinter.CTkLabel(rc_calc_result,text=str(maxlongitudinalstress)+ " MPa").grid(row=10,column=1,columnspan=2,pady=2)
    rc_maxradialstress_result = customtkinter.CTkLabel(rc_calc_result,text=str(maxradialstress)+ " MPa").grid(row=11,column=1,columnspan=2,pady=2)
    rc_effectivestress_result = customtkinter.CTkLabel(rc_calc_result,text=str(effectivestress)+ " MPa").grid(row=12,column=1,columnspan=2,pady=2)
    rc_effectivestress_unitycheck.grid(row=13,column=1,columnspan=2,pady=2)
    rc_girthallow.grid(row=14,column=1,columnspan=2,pady=2)
    rc_girthunitycheck.grid(row=15,column=1,columnspan=2,pady=2)
    rc_longallow.grid(row=16,column=1,columnspan=2,pady=2)
    rc_longunitycheck.grid(row=17,column=1,columnspan=2,pady=2)

    if barlowunitycheck == effectivestress_unitycheck == girthunitycheck == longunitycheck == "SAFE":
        rc_summary ="Safe to Install Without Pipe Casing"
        rc_summary_label = customtkinter.CTkLabel(rc_calc_result, text=rc_summary)
    else:
        rc_summary = "Need Pipe Casing"
        rc_summary_label = customtkinter.CTkLabel(rc_calc_result, text=rc_summary, width=196)

    rc_summary_label.grid(row=18,column=1,columnspan=2,pady=2)

#LabelFrame Definition
welcome=LabelFrame(root)
welcome.pack(padx=10, pady=10)

calc_select=LabelFrame(root, text="Select Calculator Module", padx=5, pady=5)
supp_calc_def=LabelFrame(root, text="Module Description", padx=5, pady=5)
rc_calc_def=LabelFrame(root, text="Module Description", padx=5, pady=5)

supp_calc_frame=LabelFrame(root, text="Pipe Support Spacing Calculator", padx=10, pady=10)
supp_calc_result=LabelFrame(root, text="Calculation Results", padx=10, pady=10)

rc_calc_frame=LabelFrame(root, text="Road Crossing Calculator", padx=10, pady=10)
rc_calc_result=LabelFrame(root, text="Calculation Results", padx=10, pady=10)

#Frame Definition
calc_opt_frame=Frame(calc_select)
supp_desc_frame=Frame(supp_calc_def, height=800, width=800)
rc_desc_frame=Frame(rc_calc_def, height=800, width=800)

#Image Definition
about=ImageTk.PhotoImage(Image.open("about.png"))
about_label=Label(welcome, image=about, padx=10, pady=10)
about_label.pack()

desc_supp = ImageTk.PhotoImage(Image.open("suppdesc.png"))
supp_desc_label = Label(supp_desc_frame, image=desc_supp, padx=10, pady=10)
supp_desc_label.pack()

desc_rc = ImageTk.PhotoImage(Image.open("rcdesc.png"))
rc_desc_label = Label(rc_desc_frame, image=desc_rc, padx=10, pady=10)
rc_desc_label.pack()

#Label Definition
code_label=customtkinter.CTkLabel(supp_calc_frame, text="Standard Code: ", padx=10).grid(row=0, column=0, pady=2)

lc_label=customtkinter.CTkLabel(supp_calc_frame, text="Location Class: ")

class_label=customtkinter.CTkLabel(supp_calc_frame, text="Pipe Material Class: ").grid(row=3, column=0, pady=2)

nps_label=customtkinter.CTkLabel(supp_calc_frame, text="Pipe NPS (in): ").grid(row=4, column=0, pady=2)

thk_label=customtkinter.CTkLabel(supp_calc_frame, text="Pipe Thickness (mm): ").grid(row=5, column=0, pady=2)

excoat_exist_label=customtkinter.CTkLabel(supp_calc_frame, text="Any External Coating Existence?").grid(row=6, column=0, pady=2)
excoat_thk_label=customtkinter.CTkLabel(supp_calc_frame, text="External Coating Thickness (mm): ")
excoat_density_label=customtkinter.CTkLabel(supp_calc_frame, text="External Coating Density (kg/m3): ")

insul_exist_label=customtkinter.CTkLabel(supp_calc_frame, text="Any Insulation Existence?").grid(row=9, column=0, pady=2)
insul_thk_label=customtkinter.CTkLabel(supp_calc_frame, text="Insulation Thickness (mm): ")
insul_density_label=customtkinter.CTkLabel(supp_calc_frame, text="Insulation Density (kg/m3): ")

incoat_exist_label=customtkinter.CTkLabel(supp_calc_frame, text="Any Internal Coating Existence?").grid(row=12, column=0, pady=2)
incoat_thk_label=customtkinter.CTkLabel(supp_calc_frame, text="Internal Coating Thickness (mm): ")
incoat_density_label=customtkinter.CTkLabel(supp_calc_frame, text="Internal Coating Density (kg/m3): ")

deflection_label=customtkinter.CTkLabel(supp_calc_frame, text="Permissible Deflection at Midspan (mm): ").grid(row=15, column=0, pady=2)

rc_code_label=customtkinter.CTkLabel(rc_calc_frame, text="Standard Code: ", padx=10).grid(row=0, column=0, pady=2)

rc_lc_label=customtkinter.CTkLabel(rc_calc_frame, text="Location Class: ")

rc_class_label=customtkinter.CTkLabel(rc_calc_frame, text="Pipe Material Class: ").grid(row=3, column=0, pady=2)

rc_nps_label=customtkinter.CTkLabel(rc_calc_frame, text="Pipe NPS (in): ").grid(row=4, column=0, pady=2)

rc_thk_label=customtkinter.CTkLabel(rc_calc_frame, text="Pipe Thickness (mm): ").grid(row=5, column=0, pady=2)

rc_excoat_thk_label=customtkinter.CTkLabel(rc_calc_frame, text="External Coating Thickness (mm): ").grid(row=6, column=0, pady=2)

rc_maop_label=customtkinter.CTkLabel(rc_calc_frame, text="Max. Operating Pressure (psi): ").grid(row=7, column=0, pady=2)

rc_maot_label=customtkinter.CTkLabel(rc_calc_frame, text="Max. Operating Temperature (deg.C): ").grid(row=8, column=0, pady=2)

rc_ambtemp_label=customtkinter.CTkLabel(rc_calc_frame, text="Ambient Temperature (deg.C): ").grid(row=9, column=0, pady=2)

rc_soiltype_label=customtkinter.CTkLabel(rc_calc_frame, text="Soil Type: ").grid(row=10, column=0, pady=2)

rc_soilunit_label=customtkinter.CTkLabel(rc_calc_frame, text="Unit Weight of Soil (kN/m3): ").grid(row=11, column=0, pady=2)

rc_soilreaction_label=customtkinter.CTkLabel(rc_calc_frame, text="Modulus of Soil Reaction (ksi): ").grid(row=12, column=0, pady=2)
rc_soilreactioninfo_label=customtkinter.CTkLabel(rc_calc_frame, text="*Refer to Annex A.1 Table A-1 of API 1102", padx=10).grid(row=12, column=3, pady=2)

rc_resilientsoil_label=customtkinter.CTkLabel(rc_calc_frame, text="Resilient Modulus of Soil (ksi): ").grid(row=13, column=0, pady=2)
rc_resilientsoilinfo_label=customtkinter.CTkLabel(rc_calc_frame, text="*Refer to Annex A.1 Table A-2 of API 1102", padx=10).grid(row=13, column=3, pady=2)

rc_pavement_label=customtkinter.CTkLabel(rc_calc_frame, text="Pavement Type: ").grid(row=14, column=0, pady=2)

rc_contactarea_label=customtkinter.CTkLabel(rc_calc_frame, text="Contact Area of Wheel: ").grid(row=15, column=0, pady=2)
rc_contactareainput_label=customtkinter.CTkLabel(rc_calc_frame, text="Contact Area of Wheel (m2): ")
rc_contactareainfo_label=customtkinter.CTkLabel(rc_calc_frame, text="*See Section 4.7.2.2.1 of API 1102").grid(row=15, column=3, pady=2)

rc_axleload_label=customtkinter.CTkLabel(rc_calc_frame, text="Axle Load: ").grid(row=17, column=0, pady=2)
rc_axleloadinput_label=customtkinter.CTkLabel(rc_calc_frame, text="Axle Load (kN): ")
rc_axleloadinfo_label=customtkinter.CTkLabel(rc_calc_frame, text="*See Section 4.7.2.2.1 of API 1102").grid(row=17, column=3, pady=2)

rc_burial_label=customtkinter.CTkLabel(rc_calc_frame, text="Pipe Burial Depth to Top of Pipe (m): ").grid(row=19, column=0, pady=2)

rc_allowablestress_label=customtkinter.CTkLabel(rc_calc_result, text="Allowable Stress: ").grid(row=0, column=0, pady=2)
rc_result_barlowstress_label=customtkinter.CTkLabel(rc_calc_result, text="Barlow Stress: ").grid(row=1, column=0, pady=2)
rc_result_ucbarlowstress_label=customtkinter.CTkLabel(rc_calc_result, text="Barlow Stress Unity Check: ").grid(row=2, column=0, pady=2)
rc_circuminternalstress_label=customtkinter.CTkLabel(rc_calc_result, text="Circumferential Internal Pressure: ").grid(row=3, column=0, pady=2)
rc_circumstress_label=customtkinter.CTkLabel(rc_calc_result, text="Circumferential Stress Due to Earth Load: ").grid(row=4, column=0, pady=2)
rc_surfaceload_label=customtkinter.CTkLabel(rc_calc_result, text="Applied Surface Load: ").grid(row=5, column=0, pady=2)
rc_impactfactor_label=customtkinter.CTkLabel(rc_calc_result, text="Impact Factor: ").grid(row=6, column=0, pady=2)
rc_cycliccircum_stress_label=customtkinter.CTkLabel(rc_calc_result, text="Cyclic Circumferential Stress: ").grid(row=7, column=0, pady=2)
rc_cycliclong_stress_label=customtkinter.CTkLabel(rc_calc_result, text="Cyclic Longitudinal Stress: ").grid(row=8, column=0, pady=2)
rc_maxcircumstress_label=customtkinter.CTkLabel(rc_calc_result, text="Max. Circumferential Stress: ").grid(row=9, column=0, pady=2)
rc_maxlongstress_label=customtkinter.CTkLabel(rc_calc_result, text="Max. Longitudinal Stress: ").grid(row=10, column=0, pady=2)
rc_maxradialstress_label=customtkinter.CTkLabel(rc_calc_result, text="Max. Radial Stress: ").grid(row=11, column=0, pady=2)
rc_effectivestress_label=customtkinter.CTkLabel(rc_calc_result, text="Effective Stress: ").grid(row=12, column=0, pady=2)
rc_effstressunity_label=customtkinter.CTkLabel(rc_calc_result, text="Effective Stress Unity Check: ").grid(row=13, column=0, pady=2)
rc_girthlimit_label=customtkinter.CTkLabel(rc_calc_result, text="Girth Weld Fatigue Limit: ").grid(row=14, column=0, pady=2)
rc_girthunity_label=customtkinter.CTkLabel(rc_calc_result, text="Girth Weld Fatigue Check: ").grid(row=15, column=0, pady=2)
rc_longlimit_label=customtkinter.CTkLabel(rc_calc_result, text="Longitudinal Weld Fatigue Limit: ").grid(row=16, column=0, pady=2)
rc_longunity_label=customtkinter.CTkLabel(rc_calc_result, text="Longitudinal Weld Fatigue Check: ").grid(row=17, column=0, pady=2)

rc_assessment_label=customtkinter.CTkLabel(rc_calc_result, text="Assessment Result: ").grid(row=18, column=0, pady=2)

#Variable Definition
calc_opt_click=customtkinter.StringVar()
code_click=customtkinter.StringVar()
lc_click=customtkinter.StringVar()
thickness_input=customtkinter.StringVar()
class_click=customtkinter.StringVar()
nps_click=customtkinter.StringVar()
excoat_click=customtkinter.StringVar()
excoat_thk_input=customtkinter.StringVar()
excoat_dens_input=customtkinter.StringVar()
incoat_click=customtkinter.StringVar()
incoat_thk_input=customtkinter.StringVar()
incoat_dens_input=customtkinter.StringVar()
insul_click=customtkinter.StringVar()
insul_thk_input=customtkinter.StringVar()
insul_dens_input=customtkinter.StringVar()
def_input=customtkinter.StringVar()
rc_soil_click=customtkinter.StringVar()
rc_pavement_click=customtkinter.StringVar()
rc_contactarea_click=customtkinter.StringVar()
rc_axleload_click=customtkinter.StringVar()
rc_code_click=customtkinter.StringVar()
rc_lc_click=customtkinter.StringVar()
rc_thickness_input=customtkinter.StringVar()
rc_class_click=customtkinter.StringVar()
rc_nps_click=customtkinter.StringVar()

#Option Definition
calc_opt_opt = ["Onshore Pipe Support Spacing Calculator",
                "Onshore Pipeline Wall Thickness Calculator",
                "Offshore Pipeline Wall Thickness Calculator",
                "Onshore Pipeline Road Crossing Calculator"]
code_op=["ASME B31.4", "ASME B31.8"]
lc_op=["Location Class 1, Div. 1", "Location Class 1, Div. 2", "Location Class 2", "Location Class 3", "Location Class 4"]
class_op=["API 5L Gr. A", "API 5L Gr. B", "API 5L X42", "API 5L X46", "API 5L X52", "API 5L X56", "API 5L X60", "API 5L X65", "API 5L X70", "API 5L X80"]
nps_op=["1/8", "1/4", "1 1/4", "1/2", "3/4", "1", "1 1/4", "1 1/2", "2", "2 1/2", "3", "4", "6", "8", "10", "12", "14",
        "16", "18", "20", "22", "24", "26", "28", "30", "32", "34", "36", "38", "40", "42", "44", "46", "48", "52", "56",
        "60", "64", "68", "72", "76", "80"]
excoat_op=["yes", "no"]
incoat_op=["yes", "no"]
insul_op=["yes", "no"]

rc_soil_op=["Loose to medium dense sands and gravels; soft clays and silts",
            "Dense to very dense sands and gravels; medium to very stiff clays and silts"]
rc_pavement_op=["No Pavement", "Flexible Pavement", "Rigid Pavement"]
rc_contactarea_op=["API Standard", "User Defined"]
rc_axleload_op=["API Standard", "User Defined"]

#Dropdown Definition
code_drop=customtkinter.CTkComboBox(supp_calc_frame, variable=code_click, values=code_op, command=code_sel).grid(row=0, column=1, columnspan=2, pady=2)
lc_drop=customtkinter.CTkComboBox(supp_calc_frame, variable=lc_click, values=lc_op, command=lc_sel)
class_drop=customtkinter.CTkComboBox(supp_calc_frame, variable=class_click, values=class_op, command=class_sel).grid(row=3, column=1, columnspan=2, pady=2)
nps_drop=customtkinter.CTkComboBox(supp_calc_frame, variable=nps_click, values=nps_op, command=nps_sel).grid(row=4, column=1, columnspan=2, pady=2)
excoat_drop=customtkinter.CTkComboBox(supp_calc_frame, variable=excoat_click, values=excoat_op, command=excoat_sel).grid(row=6, column=1, columnspan=2, pady=2)
insul_drop=customtkinter.CTkComboBox(supp_calc_frame, variable=insul_click, values=insul_op, command=insul_sel).grid(row=9, column=1, columnspan=2, pady=2)
incoat_drop=customtkinter.CTkComboBox(supp_calc_frame, variable=incoat_click, values=incoat_op, command=incoat_sel).grid(row=12, column=1, columnspan=2, pady=2)
calc_opt_drop = customtkinter.CTkComboBox(calc_opt_frame, variable=calc_opt_click, values=calc_opt_opt, command=calc_opt_sel, width=300)

rc_code_drop=customtkinter.CTkComboBox(rc_calc_frame, variable=rc_code_click, values=code_op, command=rc_code_sel).grid(row=0, column=1, columnspan=2, pady=2)
rc_lc_drop=customtkinter.CTkComboBox(rc_calc_frame, variable=rc_lc_click, values=lc_op, command=rc_lc_sel)
rc_class_drop=customtkinter.CTkComboBox(rc_calc_frame, variable=rc_class_click, values=class_op, command=rc_class_sel).grid(row=3, column=1, columnspan=2, pady=2)
rc_nps_drop=customtkinter.CTkComboBox(rc_calc_frame, variable=rc_nps_click, values=nps_op, command=rc_nps_sel).grid(row=4, column=1, columnspan=2, pady=2)
rc_soiltype_drop=customtkinter.CTkComboBox(rc_calc_frame, variable=rc_soil_click, values=rc_soil_op, command=soil_sel).grid(row=10, column=1, columnspan=2, pady=2)
rc_pavement_drop=customtkinter.CTkComboBox(rc_calc_frame, variable=rc_pavement_click, values=rc_pavement_op, command=pavement_sel).grid(row=14, column=1, columnspan=2, pady=2)
rc_contactarea_drop=customtkinter.CTkComboBox(rc_calc_frame, variable=rc_contactarea_click, values=rc_contactarea_op, command=contactarea_sel).grid(row=15, column=1, columnspan=2, pady=2)
rc_axleload_drop=customtkinter.CTkComboBox(rc_calc_frame, variable=rc_axleload_click, values=rc_axleload_op, command=axleload_sel).grid(row=17, column=1, columnspan=2, pady=2)


#Entrybox Definition
thickness_entry=customtkinter.CTkEntry(supp_calc_frame, justify= CENTER, width=140)
thickness_entry.grid(row=5, column=1, columnspan=2, pady=2)

excoat_thk_entry=customtkinter.CTkEntry(supp_calc_frame, justify= CENTER, width=140)
excoat_dens_entry=customtkinter.CTkEntry(supp_calc_frame, justify= CENTER, width=140)

incoat_thk_entry=customtkinter.CTkEntry(supp_calc_frame, justify= CENTER, width=140)
incoat_dens_entry=customtkinter.CTkEntry(supp_calc_frame, justify= CENTER, width=140)

insul_thk_entry=customtkinter.CTkEntry(supp_calc_frame, justify= CENTER,width=140)
insul_dens_entry=customtkinter.CTkEntry(supp_calc_frame, justify= CENTER, width=140)

def_entry=customtkinter.CTkEntry(supp_calc_frame, justify= CENTER, width=140)
def_entry.grid(row=15, column=1, columnspan=2, pady=2)

rc_thickness_entry=customtkinter.CTkEntry(rc_calc_frame, justify= CENTER, width=140)
rc_thickness_entry.grid(row=5, column=1, columnspan=2, pady=2)

rc_excoat_thk_entry=customtkinter.CTkEntry(rc_calc_frame, justify= CENTER, width=140)
rc_excoat_thk_entry.grid(row=6, column=1, columnspan=2, pady=2)

rc_maop_entry=customtkinter.CTkEntry(rc_calc_frame, justify= CENTER, width=140)
rc_maop_entry.grid(row=7, column=1, columnspan=2, pady=2)

rc_maot_entry=customtkinter.CTkEntry(rc_calc_frame, justify= CENTER, width=140)
rc_maot_entry.grid(row=8, column=1, columnspan=2, pady=2)

rc_ambtemp_entry=customtkinter.CTkEntry(rc_calc_frame, justify= CENTER, width=140)
rc_ambtemp_entry.grid(row=9, column=1, columnspan=2, pady=2)

rc_soilunit_entry=customtkinter.CTkEntry(rc_calc_frame, justify= CENTER, width=140)
rc_soilunit_entry.grid(row=11, column=1, columnspan=2, pady=2)

rc_soilreaction_entry=customtkinter.CTkEntry(rc_calc_frame, justify= CENTER, width=140)
rc_soilreaction_entry.grid(row=12, column=1, columnspan=2, pady=2)

rc_resilientsoil_entry=customtkinter.CTkEntry(rc_calc_frame, justify= CENTER, width=140)
rc_resilientsoil_entry.grid(row=13, column=1, columnspan=2, pady=2)

rc_contactarea_entry=customtkinter.CTkEntry(rc_calc_frame, justify= CENTER, width=140)

rc_axleload_entry=customtkinter.CTkEntry(rc_calc_frame, justify= CENTER, width=140)

rc_burial_entry=customtkinter.CTkEntry(rc_calc_frame, justify= CENTER, width=140)
rc_burial_entry.grid(row=19, column=1, columnspan=2, pady=2)


#Logo Definition
wa=Image.open("wa.png")
wa_logo=ImageTk.PhotoImage(wa)
wa_logo.image=wa_logo
email=Image.open("email.png")
email_logo=ImageTk.PhotoImage(email)


#Button Definition
start=customtkinter.CTkButton(welcome, text="Start Calculator >>", corner_radius=5, command=begin)
start.pack(side=RIGHT, padx=10, pady=10)

submit_button=customtkinter.CTkButton(supp_calc_frame, corner_radius=5, text="Submit Data and Calculate!", command=sub_calc).grid(row=16, column=1, columnspan=2, pady=10)

supp_backbutton=customtkinter.CTkButton(root, corner_radius=5, pady=5, text="Back to Main Menu", fg_color="gray75", command=back)
rc_backbutton=customtkinter.CTkButton(root, corner_radius=5, pady=5, text="Back to Main Menu", fg_color="gray75", command=back)

start_calc = customtkinter.CTkButton(calc_opt_frame, text="Select Module >>", corner_radius=5, command=calculator_start)

wa_button=customtkinter.CTkButton(welcome, image=wa_logo, text="Contact Me!", fg_color="gray75", command=contact_wa).pack(side=LEFT, padx=10, pady=10)
email_button=customtkinter.CTkButton(welcome, image=email_logo, text="Email Me!", fg_color="gray75", command=contact_email).pack(side=LEFT, padx=10, pady=10)

rc_submit_button=customtkinter.CTkButton(rc_calc_frame, corner_radius=5, text="Submit Data and Calculate!", command=rc_calc).grid(row=20, column=2, pady=10)


root.mainloop()

