# -*- coding: utf-8 -*-
"""Contact.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yaxkHyQdM4DK3dUaq1P6-oWs4mIEtTeS

#Classe di un Contatto di rubrica
Gestisce la creazione, stampa ed edit di un contatto
"""

class Contact:
    def __init__(self, name, surname, phone_number):
      """
      Crea un nuovo record di rubrica.
      :param name: Nome del contatto.
      :param surname: Cognome del contatto.
      :param phone_number: Numero di telefono del contatto.
      """
      self._name = name
      self._surname = surname
      self._phone_number = phone_number

    def __str__(self):
      """
      Restituisce una rappresentazione testuale del contatto.
      :return: Stringa contenente i dati del contatto.
      """
      return f"{self._name} {self._surname}, Phone: {self._phone_number}"

    @property
    def name(self):
      """
      Restituisce il nome del contatto.
      :return: Nome del contatto.
      """
      return self._name

    @property
    def surname(self):
      """
      Restituisce il cognome del contatto.
      :return: Cognome del contatto.
      """
      return self._surname

    @property
    def phone_number(self):
      """
      Restituisce il numero di telefono del contatto.
      :return: Numero di telefono del contatto.
      """
      return self._phone_number

    def edit_contact(self, new_name, new_surname, new_phone_number):
        """
        Modifica i dati di un contatto esistente.
        :param new_name: Nuovo nome del contatto.
        :param new_surname: Nuovo cognome del contatto.
        :param new_phone_number: Nuovo numero di telefono del contatto.
        """
        self._name = new_name
        self._surname = new_surname
        self._phone_number = new_phone_number

    def edit_name(self, newn):
        """
        Modifica il nome di un contatto esistente.
        :param newn: Nuovo nome del contatto.
        """
        self._name = newn

    def edit_surname(self, news):
        """
        Modifica il cognome di un contatto esistente.
        :param news: Nuovo cognome del contatto.
        """
        self._surname = news

    def edit_phone_number(self, newnm):
        """
        Modifica il numero di telefono di un contatto esistente.
        :param newnm: Nuovo numero di telefono del contatto.
        """
        self._phone_number = newnm

"""Testing"""

if __name__ == "__main__":

  help(Contact)

  contact = Contact("John", "Doe", "1234567890")
  print(f"Name is {contact.name}")
  print(contact.surname)
  print(contact.phone_number)
  contact.edit_contact("Jane", "Smith", "0987654321")
  print(contact)