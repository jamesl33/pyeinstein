#!/usr/bin/env python3
"""
This file is part of pyeinstein.

Copyright (C) 2019, James Lee <jamesl33info@gmail.com>.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

class House:
    def __init__(self):
        self.color = None
        self.nationality = None
        self.pet = None
        self.smoke = None
        self.drink = None


def check(houses):
    for index, house in enumerate(houses):
        # nationalities
        if house.nationality == 'brit':
            assert house.color == 'red'
        elif house.nationality == 'swede':
            assert house.pet == 'dog'
        elif house.nationality == 'dane':
            assert house.drink == 'tea'
        elif house.nationality == 'ger':
            assert house.smoke == 'prince'
        elif house.nationality == 'nor':
            if index == 0:
                assert houses[index + 1].color == 'blue'
            elif index == 4:
                assert houses[index - 1].color == 'blue'
            else:
                assert houses[index - 1].color == 'blue' or houses[index + 1] == 'blue'

        # colors
        if house.color == 'green':
            assert index < 4 and houses[index + 1].color == 'white'
            assert house.drink == 'coffee'
        elif house.color == 'yellow':
            assert house.smoke == 'dunhill'

        # smokes
        if house.smoke == 'pallmall':
            assert house.pet == 'bird'
        elif house.smoke == 'blends':
            if index == 0:
                assert houses[index + 1].pet == 'cat'
            elif index == 4:
                assert houses[index - 1].pet == 'cat'
            else:
                assert houses[index - 1].pet == 'cat' or houses[index + 1].pet == 'cat'

            if index == 0:
                assert houses[index + 1].drink == 'water'
            elif index == 4:
                assert houses[index - 1].drink == 'water'
            else:
                assert houses[index - 1].drink == 'water' or houses[index + 1].drink == 'water'
        elif house.smoke == 'dunhill':
            if index == 0:
                assert houses[index + 1].pet == 'horse'
            elif index == 4:
                assert houses[index - 1].pet == 'horse'
            else:
                assert houses[index - 1].pet == 'horse' or houses[index + 1].pet == 'horse'
        elif house.smoke == 'bluemaster':
            assert house.drink == 'beer'

        # position
        if index == 2:
            assert house.drink == 'milk'
        elif index == 0:
            assert house.nationality == 'nor'

    for house in houses:
        if house.pet == 'fish':
            print(house.nationality)


houses = [House(), House(), House(), House(), House()]


houses[0].nationality = 'nor'
houses[0].color = 'yellow'
houses[0].pet = 'cat'
houses[0].smoke = 'dunhill'
houses[0].drink = 'water'

houses[1].nationality = 'dane'
houses[1].color = 'blue'
houses[1].pet = 'horse'
houses[1].smoke = 'blends'
houses[1].drink = 'tea'

houses[2].nationality = 'brit'
houses[2].color = 'red'
houses[2].pet = 'bird'
houses[2].smoke = 'pallmall'
houses[2].drink = 'milk'

houses[3].nationality = 'ger'
houses[3].color = 'green'
houses[3].pet = 'fish'
houses[3].smoke = 'prince'
houses[3].drink = 'coffee'

houses[4].nationality = 'swede'
houses[4].color = 'white'
houses[4].pet = 'dog'
houses[4].smoke = 'bluemaster'
houses[4].drink = 'beer'


check(houses)
