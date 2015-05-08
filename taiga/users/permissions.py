# Copyright (C) 2014 Andrey Antukh <niwi@niwi.be>
# Copyright (C) 2014 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014 David Barragán <bameda@dbarragan.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from taiga.base.api.permissions import TaigaResourcePermission
from taiga.base.api.permissions import IsSuperUser
from taiga.base.api.permissions import AllowAny
from taiga.base.api.permissions import IsAuthenticated
from taiga.base.api.permissions import HasProjectPerm
from taiga.base.api.permissions import IsProjectOwner
from taiga.base.api.permissions import PermissionComponent


class IsTheSameUser(PermissionComponent):
    def check_permissions(self, request, view, obj=None):
        return obj and request.user.is_authenticated() and request.user.pk == obj.pk


class UserPermission(TaigaResourcePermission):
    enought_perms = IsSuperUser()
    global_perms = None
    retrieve_perms = IsTheSameUser()
    update_perms = IsTheSameUser()
    destroy_perms = IsTheSameUser()
    list_perms = AllowAny()
    stats_perms = AllowAny()
    password_recovery_perms = AllowAny()
    change_password_from_recovery_perms = AllowAny()
    change_password_perms = IsAuthenticated()
    change_avatar_perms = IsAuthenticated()
    me_perms = IsAuthenticated()
    remove_avatar_perms = IsAuthenticated()
    starred_perms = AllowAny()
    change_email_perms = IsTheSameUser()
    contacts_perms = AllowAny()


class RolesPermission(TaigaResourcePermission):
    retrieve_perms = HasProjectPerm('view_project')
    create_perms = IsProjectOwner()
    update_perms = IsProjectOwner()
    destroy_perms = IsProjectOwner()
    list_perms = AllowAny()
