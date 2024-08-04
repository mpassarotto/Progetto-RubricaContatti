# -*- coding: utf-8 -*-
"""ContactsManager.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xHd6O6ZfSeMEZC8tnf_Z-HLwQkF4KpuA
"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/Colab Notebooks/Progetto - Rubrica contatti

from contact import Contact
import csv

from enum import Enum
class Action(Enum):
    Exit = 0
    Load = 1
    Save = 2
    Add = 3
    Edit = 4
    Delete = 5
    Print = 6
    Name = 7
    Surname = 8
    Phone = 9
    All = 10
    Null = 11

class ContactsManager:
    def __init__(self):
      """
      Costruttore rubrica vuota
      - _contacts: member privato dei contatti, fa init a vuotone
      - _pending_changes: member privato che indica se ci sono modifiche da salvare
      """
      self._contacts = {}
      self._pending_changes = False

    @property
    def pending_changes(self):
      """
      Public property. If true ci sono modifiche da salvare
      """
      return self._pending_changes

    def add_contact(self, contact, silent = False):
      """
      Aggiunge un contatto alla rubrica
      """
      exist = self._contains_key(self._get_hash(contact))
      validnum = self._valid_num(contact.phone_number)
      if (exist):
        if (not silent): print("Already existing contact")
      else:
        if (not validnum):
          if (not silent): print("Invalid phone number!")
        else:
          self._contacts[self._get_hash(contact)] = contact
          if (not silent): print(" >>> Added!")
      return exist and validnum

    def remove_contact(self, contact):
      """
      Rimuove un contatto dalla rubrica
      """
      key = self._get_hash(contact)
      exist = self._contains_key(key)
      if (not exist):
        print("Contact not found!")
      else:
        self._contacts.pop(key)
        self._pending_changes = True
        print(" >>> Removed!")
      return exist

    def update_contact(self, contact, new_contact):
      """
      Aggiorna un contatto delle rubrica sostitutendolo
      """
      self.remove_contact(contact)
      self.add_contact(new_contact)
      self._pending_changes = True
      print(" >>> Updated contact!")

    def update_name(self, contact, new_name):
      """
      Aggiorna il nome di un contatto nella rubrica
      """
      self._contacts[self._get_hash(contact)].edit_name(new_name)
      self._pending_changes = True
      print(" >>> Updated name!")

    def update_surname(self, contact, new_surname):
      """
      Aggiorna il cognome di un contatto nella rubrica
      """
      self._contacts[self._get_hash(contact)].edit_surname(new_surname)
      self._pending_changes = True
      print(" >>> Updated surname!")

    def update_phone(self, contact, new_num):
      """
      Aggiorna il numero di telefono di un contatto nella rubrica
      """
      if (self._valid_num(new_num)):
        self._contacts[self._get_hash(contact)].edit_phone_number(new_num)
        self._pending_changes = True
        print(" >>> Updated phone!")

    def get_all_contacts(self):
      """
      Restituisce tutti i contatti della rubrica
      """
      allc = self._get_sorted()
      self.print_contacts_list(allc)
      return allc

    def get_contacts_by_name(self, name):
      """
      Restituisce tutti i contatti della rubrica con il nome specificato
      """
      founds = []
      for record in self._contacts.keys():
          if record.endswith(name):
            founds.append(self._contacts[record])
      self.print_contacts_list(founds)
      return founds

    def get_contacts_by_surname(self, surname):
      """
      Restituisce tutti i contatti della rubrica con il cognome specificato
      """
      founds = []
      for record in self._contacts.keys():
          if record.startswith(surname):
            founds.append(self._contacts[record])
      self.print_contacts_list(founds)
      return founds

    def get_contacts_by_phone(self, phone):
      """
      Restituisce tutti i contatti della rubrica con il numero specificato
      """
      founds = []
      for record in self._contacts.keys():
          if self._contacts[record].phone_number == phone:
            founds.append(self._contacts[record])
      if len(founds) == 0:
        print("Warning: no matching phone number!")
      elif len(founds) > 1:
        print("Fatal Error: inconsistent phone numbers in the book!")
      self.print_contacts_list(founds)
      return founds

    def get_contact(self, name, surname):
      """
      Restituisce il contatto della rubrica con il nome e il cognome specificati
      """
      return self._contacts[self._get_hash_string(name, surname)]

    def print_contacts_list(self, contacts):
      """
      Stampa una lista di contatti passata come parametro
      """
      if (len(contacts) == 0):
        print("No contacts found!")
        return False
      else:
        print("\nContacts:")
        i = 1
        for contact in contacts:
          print(f"#{i} - {contact}")
          i += 1
        return True

    def export_contacts(self,filename):
      """
      Export all contacts to csv file
      """
      with open(filename + '.csv', 'w', newline='') as csvfile:
          writer = csv.writer(csvfile)
          writer.writerow(['Surname', 'Name', 'Phone Number'])
          for contact in self._get_sorted():
              writer.writerow([contact.surname, contact.name, contact.phone_number])
      self._pending_changes = False

    def import_contacts(self,filename):
      """
      Importa contacts da file csv [Surname, Name, Phone Number]
      """
      self._contacts = {}
      with open(filename + '.csv', 'r') as csvfile:
          reader = csv.reader(csvfile)
          for row in reader:
            contact = Contact(row[1], row[0], row[2])
            self.add_contact(contact, silent = True)
      if len(self._contacts) > 0:
        print(" >> Imported: ")
        self.get_all_contacts()

################################################################################
# PRIVATE:
################################################################################
    def _get_hash(self, contact):
      return self._get_hash_string(contact.name, contact.surname)

    def _get_hash_string(self, name, surname):
      return surname + name

    def _contains_key(self, key):
      return key in self._contacts.keys()

    def _valid_num(self, num):
      alreadyexist = False
      for contact in self._contacts.values():
          if contact.phone_number == num:
              alreadyexist = True
              break

          if (num.isdigit() == False): print("Invalid phone format!")
          elif (len(num) != 10): print("Phone number must contains 10 digits!")
          elif (alreadyexist): print("Phone number already exists!")
      return num.isdigit() and len(num) == 10 and not alreadyexist

    def _get_sorted(self):
      return list(dict(sorted(self._contacts.items())).values())

"""Testing contacts manager:"""

if __name__ == "__main__":
    contacts = ContactsManager()

    contacts.import_contacts('BUora')
    # contacts.add_contact(Contact("Pippo", "Auriemme", "1234567890"))
    # contacts.add_contact(Contact("Pippo", "Betlemme", "1234567891"))
    # contacts.add_contact(Contact("Pippo", "Cappero", "1234567895"))
    # contacts.add_contact(Contact("Giuseppe", "Cappero", "1234567897"))

    contacts.get_all_contacts()
    # for contact in contacts.get_contacts_by_name("Giuseppe"):
    #     print(contact)

    # contacts.export_contacts("BU20240729")

"""Classe del menu"""

from types import SimpleNamespace
from time import sleep
# classetta del menu statica
class Menu():

  def MainMenu(manager, choice):
    """
    Classe statica del menu principale
    - agisce su una classe "manager" di tipo ContactsManager
    - choice è un Action
    """
    if choice == Action.Exit:
      if (manager.pending_changes):
        print("There are unsaved changes.")
        msg = input("Do you want to save them? [Y/n] ")
        if (msg == "Y"):
          filename = input("Enter filename: ")
          manager.export_contacts(filename)
      print("Exiting...")
      return None
    elif choice == Action.Load:
      filename = input("Enter filename: ")
      manager.import_contacts(filename)
    elif choice == Action.Save:
      filename = input("Enter filename: ")
      manager.export_contacts(filename)
    elif choice == Action.Add:
      name = input("Enter name: ")
      surname = input("Enter surname: ")
      phone = input("Enter phone number: ")
      manager.add_contact(Contact(name, surname, phone))
    elif choice == Action.Edit:
      Menu._contact_editor_selector(manager, choice)
    elif choice == Action.Delete:
      Menu._contact_editor_selector(manager, choice)
    elif choice == Action.Print:
      manager.get_all_contacts()
    else:
      return None

  def _contact_editor_selector(manager, action):
      print("Contacts search init...")
      for i in range(10):
        print("#-#", end =""), # print on the same line
        sleep(1/(i + 1))

      print("\nWhat do you want to search?")
      print(" > " + Action.Name.name)
      print(" > " + Action.Surname.name)
      print(" > " + Action.Phone.name)
      print(" > " + Action.All.name)
      choice = input("\n >> ")
      founds =[]
      if (choice == Action.All.name):
        founds = manager.get_all_contacts()
        if (len(founds) == 0): return None
      elif (choice == Action.Name.name):
        name = input("Enter name: ")
        founds = manager.get_contacts_by_name(name)
        if (len(founds) == 0): return None
      elif (choice == Action.Surname.name):
        surname = input("Enter surname: ")
        founds = manager.get_contacts_by_surname(surname)
        if (len(founds) == 0): return None
      elif (choice == Action.Phone.name):
        phone = input("Enter phone number: ")
        founds = manager.get_contacts_by_phone(phone)
        if (len(founds) == 0): return None
      else:
        print("Invalid choice!")
        return None

      print("\nChoose contact ID")
      sel = founds[int(input(" >> #")) - 1]
      sel_contact = manager.get_contact(sel.name, sel.surname)
      print(f"Selected contact: {sel_contact}\n")
      go_on = input("Do you want to continue? [Y/n]")
      if (go_on == "n"): return None
      if (action.name == Action.Delete.name): # se faccio delete interrompo qui
        if (not manager.remove_contact(sel_contact)):
          print("Warning: unable to delete the contact.")
        return None

      print("What do you want to edit?")
      print(" > " + Action.Name.name)
      print(" > " + Action.Surname.name)
      print(" > " + Action.Phone.name)
      print(" > " + Action.All.name)
      choice = input("\n >> ")
      if (choice == Action.All.name):
        name = input("Enter new name: ")
        surname = input("Enter new surname: ")
        phone = input("Enter new phone number: ")
        try:
          new_contact = Contact(name, surname, phone)
          manager.update_contact(sel_contact, new_contact)
        except:
          print("Fatal Error: something went wrong when editing the whole contact.")
          return None
      elif (choice == Action.Name.name):
        name = input("Enter new name: ")
        try:
          manager.update_name(sel_contact, name)
        except:
          print("Fatal Error: something went wrong when editing the name.")
          return None
      elif (choice == Action.Surname.name):
        surname = input("Enter new surname: ")
        try:
          manager.update_surname(sel_contact, surname)
        except:
          print("Fatal Error: something went wrong when editing the surname.")
          return None
      elif (choice == Action.Phone.name):
        phone = input("Enter new phone number: ")
        try:
          manager.update_phone(sel_contact, phone)
        except:
          print("Fatal Error: something went wrong when editing the phone number.")
          return None
      else:
        print("Invalid choice!")
        return None

"""Testing menu"""

if __name__ == "__main__":
  contacts = ContactsManager()
  contacts.import_contacts('GG')
  Menu.MainMenu(contacts, Action.Load)