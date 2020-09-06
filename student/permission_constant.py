# Permissions name and code
archive_permission = (
                      '_student_can_archive_permission',
                      'Can archive permission'
                    )
all_crud_permission = (
    '_student_can_do_all_crud_permission', 'Can do all crud')
view_only_permission = (
    '_student_can_view_only_permission', 'Can view only permission')
# view_classified_information_permission = ('_student_can_view_classified_information',
#                                         'Can view classified information')
# document_management_permission = ('_student_can_upload_or_delete_documents',
#                                 'Can upload or delete documents')

# Permission list associated with groups
super_group_permissions = [archive_permission,
                           all_crud_permission, view_only_permission]
# document_management_group_permissions = [document_management_permission]
view_group_permission = [view_only_permission]
archive_group_permission = [archive_permission]

# Group names
STUDENT_SUPER_GROUP = '_student_super_group'
STUDENT_VIEW_ONLY_GROUP = '_student_view_only_group'
# PROJECT_DOCUMENT_MANAGEMENT_GROUP = '_project_document_management_group'
STUDENT_ARCHIVE_GROUP = '_student_archive_group'

# Group and permission list mappings
student_permission_group = {STUDENT_SUPER_GROUP: super_group_permissions,
                            STUDENT_VIEW_ONLY_GROUP: view_group_permission,
                            # STUDENT_DOCUMENT_MANAGEMENT_GROUP:
                            #     document_management_group_permissions,
                            STUDENT_ARCHIVE_GROUP: archive_group_permission}
