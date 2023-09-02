# trello_api_client.DefaultApi

All URIs are relative to *https://api.trello.com/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applications_key_compliance**](DefaultApi.md#applications_key_compliance) | **GET** /applications/{key}/compliance | Get Application&#x27;s compliance data
[**boards_id_checklists**](DefaultApi.md#boards_id_checklists) | **GET** /boards/{id}/checklists | Get Checklists on a Board
[**boardsidmembersidmember**](DefaultApi.md#boardsidmembersidmember) | **DELETE** /boards/{id}/members/{idMember} | Remove Member from Board
[**cardsidmembersvoted1**](DefaultApi.md#cardsidmembersvoted1) | **POST** /cards/{id}/membersVoted | Add Member vote to Card
[**delete_actions_id**](DefaultApi.md#delete_actions_id) | **DELETE** /actions/{id} | Delete an Action
[**delete_actions_idaction_reactions_id**](DefaultApi.md#delete_actions_idaction_reactions_id) | **DELETE** /actions/{idAction}/reactions/{id} | Delete Action&#x27;s Reaction
[**delete_boards_id**](DefaultApi.md#delete_boards_id) | **DELETE** /boards/{id} | Delete a Board
[**delete_boards_id_boardplugins**](DefaultApi.md#delete_boards_id_boardplugins) | **DELETE** /boards/{id}/boardPlugins/{idPlugin} | Disable a Power-Up on a Board
[**delete_cards_id**](DefaultApi.md#delete_cards_id) | **DELETE** /cards/{id} | Delete a Card
[**delete_cards_id_actions_id_comments**](DefaultApi.md#delete_cards_id_actions_id_comments) | **DELETE** /cards/{id}/actions/{idAction}/comments | Delete a comment on a Card
[**delete_cards_id_checkitem_idcheckitem**](DefaultApi.md#delete_cards_id_checkitem_idcheckitem) | **DELETE** /cards/{id}/checkItem/{idCheckItem} | Delete checkItem on a Card
[**delete_cards_id_checklists_idchecklist**](DefaultApi.md#delete_cards_id_checklists_idchecklist) | **DELETE** /cards/{id}/checklists/{idChecklist} | Delete a Checklist on a Card
[**delete_cards_id_idlabels_idlabel**](DefaultApi.md#delete_cards_id_idlabels_idlabel) | **DELETE** /cards/{id}/idLabels/{idLabel} | Remove a Label from a Card
[**delete_cards_id_membersvoted_idmember**](DefaultApi.md#delete_cards_id_membersvoted_idmember) | **DELETE** /cards/{id}/membersVoted/{idMember} | Remove a Member&#x27;s Vote on a Card
[**delete_cards_id_stickers_idsticker**](DefaultApi.md#delete_cards_id_stickers_idsticker) | **DELETE** /cards/{id}/stickers/{idSticker} | Delete a Sticker on a Card
[**delete_checklists_id**](DefaultApi.md#delete_checklists_id) | **DELETE** /checklists/{id} | Delete a Checklist
[**delete_checklists_id_checkitems_idcheckitem**](DefaultApi.md#delete_checklists_id_checkitems_idcheckitem) | **DELETE** /checklists/{id}/checkItems/{idCheckItem} | Delete Checkitem from Checklist
[**delete_customfields_id**](DefaultApi.md#delete_customfields_id) | **DELETE** /customFields/{id} | Delete a Custom Field definition
[**delete_customfields_options_idcustomfieldoption**](DefaultApi.md#delete_customfields_options_idcustomfieldoption) | **DELETE** /customFields/{id}/options/{idCustomFieldOption} | Delete Option of Custom Field dropdown
[**delete_enterprises_id_organizations_idorg**](DefaultApi.md#delete_enterprises_id_organizations_idorg) | **DELETE** /enterprises/{id}/organizations/{idOrg} | Delete an Organization from an Enterprise.
[**delete_id_idmembers_idmember**](DefaultApi.md#delete_id_idmembers_idmember) | **DELETE** /cards/{id}/idMembers/{idMember} | Remove a Member from a Card
[**delete_labels_id**](DefaultApi.md#delete_labels_id) | **DELETE** /labels/{id} | Delete a Label
[**delete_members_id_boardbackgrounds_idbackground**](DefaultApi.md#delete_members_id_boardbackgrounds_idbackground) | **DELETE** /members/{id}/boardBackgrounds/{idBackground} | Delete a Member&#x27;s custom Board background
[**delete_members_id_boardstars_idstar**](DefaultApi.md#delete_members_id_boardstars_idstar) | **DELETE** /members/{id}/boardStars/{idStar} | Delete Star for Board
[**delete_members_id_customboardbackgrounds_idbackground**](DefaultApi.md#delete_members_id_customboardbackgrounds_idbackground) | **DELETE** /members/{id}/customBoardBackgrounds/{idBackground} | Delete custom Board Background of Member
[**delete_members_id_customstickers_idsticker**](DefaultApi.md#delete_members_id_customstickers_idsticker) | **DELETE** /members/{id}/customStickers/{idSticker} | Delete a Member&#x27;s custom Sticker
[**delete_members_id_savedsearches_idsearch**](DefaultApi.md#delete_members_id_savedsearches_idsearch) | **DELETE** /members/{id}/savedSearches/{idSearch} | Delete a saved search
[**delete_organizations_id**](DefaultApi.md#delete_organizations_id) | **DELETE** /organizations/{id} | Delete an Organization
[**delete_organizations_id_logo**](DefaultApi.md#delete_organizations_id_logo) | **DELETE** /organizations/{id}/logo | Delete Logo for Organization
[**delete_organizations_id_members**](DefaultApi.md#delete_organizations_id_members) | **DELETE** /organizations/{id}/members/{idMember} | Remove a Member from an Organization
[**delete_organizations_id_prefs_associateddomain**](DefaultApi.md#delete_organizations_id_prefs_associateddomain) | **DELETE** /organizations/{id}/prefs/associatedDomain | Remove the associated Google Apps domain from a Workspace
[**delete_organizations_id_prefs_orginviterestrict**](DefaultApi.md#delete_organizations_id_prefs_orginviterestrict) | **DELETE** /organizations/{id}/prefs/orgInviteRestrict | Delete the email domain restriction on who can be invited to the Workspace
[**delete_organizations_id_tags_idtag**](DefaultApi.md#delete_organizations_id_tags_idtag) | **DELETE** /organizations/{id}/tags/{idTag} | Delete an Organization&#x27;s Tag
[**delete_token**](DefaultApi.md#delete_token) | **DELETE** /tokens/{token}/ | Delete a Token
[**delete_tokens_token_webhooks_idwebhook**](DefaultApi.md#delete_tokens_token_webhooks_idwebhook) | **DELETE** /tokens/{token}/webhooks/{idWebhook} | Delete a Webhook created by Token
[**delete_webhooks_id**](DefaultApi.md#delete_webhooks_id) | **DELETE** /webhooks/{id} | Delete a Webhook
[**deleted_cards_id_attachments_idattachment**](DefaultApi.md#deleted_cards_id_attachments_idattachment) | **DELETE** /cards/{id}/attachments/{idAttachment} | Delete an Attachment on a Card
[**emoji**](DefaultApi.md#emoji) | **GET** /emoji | List available Emoji
[**enterprises_id_members_id_member_deactivated**](DefaultApi.md#enterprises_id_members_id_member_deactivated) | **PUT** /enterprises/{id}/members/{idMember}/deactivated | Deactivate a Member of an Enterprise.
[**enterprises_id_organizations_idmember**](DefaultApi.md#enterprises_id_organizations_idmember) | **DELETE** /enterprises/{id}/admins/{idMember} | Remove a Member as admin from Enterprise.
[**get_actions_id**](DefaultApi.md#get_actions_id) | **GET** /actions/{id} | Get an Action
[**get_actions_id_board**](DefaultApi.md#get_actions_id_board) | **GET** /actions/{id}/board | Get the Board for an Action
[**get_actions_id_card**](DefaultApi.md#get_actions_id_card) | **GET** /actions/{id}/card | Get the Card for an Action
[**get_actions_id_field**](DefaultApi.md#get_actions_id_field) | **GET** /actions/{id}/{field} | Get a specific field on an Action
[**get_actions_id_list**](DefaultApi.md#get_actions_id_list) | **GET** /actions/{id}/list | Get the List for an Action
[**get_actions_id_member**](DefaultApi.md#get_actions_id_member) | **GET** /actions/{id}/member | Get the Member of an Action
[**get_actions_id_membercreator**](DefaultApi.md#get_actions_id_membercreator) | **GET** /actions/{id}/memberCreator | Get the Member Creator of an Action
[**get_actions_id_organization**](DefaultApi.md#get_actions_id_organization) | **GET** /actions/{id}/organization | Get the Organization of an Action
[**get_actions_idaction_reactions**](DefaultApi.md#get_actions_idaction_reactions) | **GET** /actions/{idAction}/reactions | Get Action&#x27;s Reactions
[**get_actions_idaction_reactions_id**](DefaultApi.md#get_actions_idaction_reactions_id) | **GET** /actions/{idAction}/reactions/{id} | Get Action&#x27;s Reaction
[**get_actions_idaction_reactionsummary**](DefaultApi.md#get_actions_idaction_reactionsummary) | **GET** /actions/{idAction}/reactionsSummary | List Action&#x27;s summary of Reactions
[**get_batch**](DefaultApi.md#get_batch) | **GET** /batch | Batch Requests
[**get_board_id_plugins**](DefaultApi.md#get_board_id_plugins) | **GET** /boards/{id}/plugins | Get Power-Ups on a Board
[**get_boards_id**](DefaultApi.md#get_boards_id) | **GET** /boards/{id} | Get a Board
[**get_boards_id_actions**](DefaultApi.md#get_boards_id_actions) | **GET** /boards/{boardId}/actions | Get Actions of a Board
[**get_boards_id_boardplugins**](DefaultApi.md#get_boards_id_boardplugins) | **GET** /boards/{id}/boardPlugins | Get Enabled Power-Ups on Board
[**get_boards_id_boardstars**](DefaultApi.md#get_boards_id_boardstars) | **GET** /boards/{boardId}/boardStars | Get boardStars on a Board
[**get_boards_id_cards**](DefaultApi.md#get_boards_id_cards) | **GET** /boards/{id}/cards | Get Cards on a Board
[**get_boards_id_cards_filter**](DefaultApi.md#get_boards_id_cards_filter) | **GET** /boards/{id}/cards/{filter} | Get filtered Cards on a Board
[**get_boards_id_cards_idcard**](DefaultApi.md#get_boards_id_cards_idcard) | **GET** /boards/{id}/cards/{idCard} | Get a Card on a Board
[**get_boards_id_customfields**](DefaultApi.md#get_boards_id_customfields) | **GET** /boards/{id}/customFields | Get Custom Fields for Board
[**get_boards_id_field**](DefaultApi.md#get_boards_id_field) | **GET** /boards/{id}/{field} | Get a field on a Board
[**get_boards_id_labels**](DefaultApi.md#get_boards_id_labels) | **GET** /boards/{id}/labels | Get Labels on a Board
[**get_boards_id_lists**](DefaultApi.md#get_boards_id_lists) | **GET** /boards/{id}/lists | Get Lists on a Board
[**get_boards_id_lists_filter**](DefaultApi.md#get_boards_id_lists_filter) | **GET** /boards/{id}/lists/{filter} | Get filtered Lists on a Board
[**get_boards_id_members**](DefaultApi.md#get_boards_id_members) | **GET** /boards/{id}/members | Get the Members of a Board
[**get_boards_id_memberships**](DefaultApi.md#get_boards_id_memberships) | **GET** /boards/{id}/memberships | Get Memberships of a Board
[**get_cards_id**](DefaultApi.md#get_cards_id) | **GET** /cards/{id} | Get a Card
[**get_cards_id_actions**](DefaultApi.md#get_cards_id_actions) | **GET** /cards/{id}/actions | Get Actions on a Card
[**get_cards_id_attachments**](DefaultApi.md#get_cards_id_attachments) | **GET** /cards/{id}/attachments | Get Attachments on a Card
[**get_cards_id_attachments_idattachment**](DefaultApi.md#get_cards_id_attachments_idattachment) | **GET** /cards/{id}/attachments/{idAttachment} | Get an Attachment on a Card
[**get_cards_id_board**](DefaultApi.md#get_cards_id_board) | **GET** /cards/{id}/board | Get the Board the Card is on
[**get_cards_id_checkitem_idcheckitem**](DefaultApi.md#get_cards_id_checkitem_idcheckitem) | **GET** /cards/{id}/checkItem/{idCheckItem} | Get checkItem on a Card
[**get_cards_id_checkitemstates**](DefaultApi.md#get_cards_id_checkitemstates) | **GET** /cards/{id}/checkItemStates | Get checkItems on a Card
[**get_cards_id_checklists**](DefaultApi.md#get_cards_id_checklists) | **GET** /cards/{id}/checklists | Get Checklists on a Card
[**get_cards_id_customfielditems**](DefaultApi.md#get_cards_id_customfielditems) | **GET** /cards/{id}/customFieldItems | Get Custom Field Items for a Card
[**get_cards_id_field**](DefaultApi.md#get_cards_id_field) | **GET** /cards/{id}/{field} | Get a field on a Card
[**get_cards_id_list**](DefaultApi.md#get_cards_id_list) | **GET** /cards/{id}/list | Get the List of a Card
[**get_cards_id_members**](DefaultApi.md#get_cards_id_members) | **GET** /cards/{id}/members | Get the Members of a Card
[**get_cards_id_membersvoted**](DefaultApi.md#get_cards_id_membersvoted) | **GET** /cards/{id}/membersVoted | Get Members who have voted on a Card
[**get_cards_id_plugindata**](DefaultApi.md#get_cards_id_plugindata) | **GET** /cards/{id}/pluginData | Get pluginData on a Card
[**get_cards_id_stickers**](DefaultApi.md#get_cards_id_stickers) | **GET** /cards/{id}/stickers | Get Stickers on a Card
[**get_cards_id_stickers_idsticker**](DefaultApi.md#get_cards_id_stickers_idsticker) | **GET** /cards/{id}/stickers/{idSticker} | Get a Sticker on a Card
[**get_checklists_id**](DefaultApi.md#get_checklists_id) | **GET** /checklists/{id} | Get a Checklist
[**get_checklists_id_board**](DefaultApi.md#get_checklists_id_board) | **GET** /checklists/{id}/board | Get the Board the Checklist is on
[**get_checklists_id_cards**](DefaultApi.md#get_checklists_id_cards) | **GET** /checklists/{id}/cards | Get the Card a Checklist is on
[**get_checklists_id_checkitems**](DefaultApi.md#get_checklists_id_checkitems) | **GET** /checklists/{id}/checkItems | Get Checkitems on a Checklist
[**get_checklists_id_checkitems_idcheckitem**](DefaultApi.md#get_checklists_id_checkitems_idcheckitem) | **GET** /checklists/{id}/checkItems/{idCheckItem} | Get a Checkitem on a Checklist
[**get_checklists_id_field**](DefaultApi.md#get_checklists_id_field) | **GET** /checklists/{id}/{field} | Get field on a Checklist
[**get_customfields_id**](DefaultApi.md#get_customfields_id) | **GET** /customFields/{id} | Get a Custom Field
[**get_customfields_id_options**](DefaultApi.md#get_customfields_id_options) | **POST** /customFields/{id}/options | Add Option to Custom Field dropdown
[**get_customfields_options_idcustomfieldoption**](DefaultApi.md#get_customfields_options_idcustomfieldoption) | **GET** /customFields/{id}/options/{idCustomFieldOption} | Get Option of Custom Field dropdown
[**get_enterprises_id**](DefaultApi.md#get_enterprises_id) | **GET** /enterprises/{id} | Get an Enterprise
[**get_enterprises_id_admins**](DefaultApi.md#get_enterprises_id_admins) | **GET** /enterprises/{id}/admins | Get Enterprise admin Members
[**get_enterprises_id_auditlog**](DefaultApi.md#get_enterprises_id_auditlog) | **GET** /enterprises/{id}/auditlog | Get auditlog data for an Enterprise
[**get_enterprises_id_claimable_organizations**](DefaultApi.md#get_enterprises_id_claimable_organizations) | **GET** /enterprises/{id}/claimableOrganizations | Get ClaimableOrganizations of an Enterprise
[**get_enterprises_id_members**](DefaultApi.md#get_enterprises_id_members) | **GET** /enterprises/{id}/members | Get Members of Enterprise
[**get_enterprises_id_members_idmember**](DefaultApi.md#get_enterprises_id_members_idmember) | **GET** /enterprises/{id}/members/{idMember} | Get a Member of Enterprise
[**get_enterprises_id_organizations_bulk_id_organizations**](DefaultApi.md#get_enterprises_id_organizations_bulk_id_organizations) | **GET** /enterprises/{id}/organizations/bulk/{idOrganizations} | Bulk accept a set of organizations to an Enterprise.
[**get_enterprises_id_pending_organizations**](DefaultApi.md#get_enterprises_id_pending_organizations) | **GET** /enterprises/{id}/pendingOrganizations | Get PendingOrganizations of an Enterprise
[**get_enterprises_id_signupurl**](DefaultApi.md#get_enterprises_id_signupurl) | **GET** /enterprises/{id}/signupUrl | Get signupUrl for Enterprise
[**get_enterprises_id_transferrable_bulk_id_organizations**](DefaultApi.md#get_enterprises_id_transferrable_bulk_id_organizations) | **GET** /enterprises/{id}/transferrable/bulk/{idOrganizations} | Get a bulk list of organizations that can be transferred to an enterprise.
[**get_enterprises_id_transferrable_organization_id_organization**](DefaultApi.md#get_enterprises_id_transferrable_organization_id_organization) | **GET** /enterprises/{id}/transferrable/organization/{idOrganization} | Get whether an organization can be transferred to an enterprise.
[**get_labels_id**](DefaultApi.md#get_labels_id) | **GET** /labels/{id} | Get a Label
[**get_lists_id**](DefaultApi.md#get_lists_id) | **GET** /lists/{id} | Get a List
[**get_lists_id_actions**](DefaultApi.md#get_lists_id_actions) | **GET** /lists/{id}/actions | Get Actions for a List
[**get_lists_id_board**](DefaultApi.md#get_lists_id_board) | **GET** /lists/{id}/board | Get the Board a List is on
[**get_lists_id_cards**](DefaultApi.md#get_lists_id_cards) | **GET** /lists/{id}/cards | Get Cards in a List
[**get_members_id_actions**](DefaultApi.md#get_members_id_actions) | **GET** /members/{id}/actions | Get a Member&#x27;s Actions
[**get_members_id_boardbackgrounds**](DefaultApi.md#get_members_id_boardbackgrounds) | **GET** /members/{id}/boardBackgrounds | Get Member&#x27;s custom Board backgrounds
[**get_members_id_boardbackgrounds_idbackground**](DefaultApi.md#get_members_id_boardbackgrounds_idbackground) | **GET** /members/{id}/boardBackgrounds/{idBackground} | Get a boardBackground of a Member
[**get_members_id_boards**](DefaultApi.md#get_members_id_boards) | **GET** /members/{id}/boards | Get Boards that Member belongs to
[**get_members_id_boardsinvited**](DefaultApi.md#get_members_id_boardsinvited) | **GET** /members/{id}/boardsInvited | Get Boards the Member has been invited to
[**get_members_id_boardstars**](DefaultApi.md#get_members_id_boardstars) | **GET** /members/{id}/boardStars | Get a Member&#x27;s boardStars
[**get_members_id_boardstars_idstar**](DefaultApi.md#get_members_id_boardstars_idstar) | **GET** /members/{id}/boardStars/{idStar} | Get a boardStar of Member
[**get_members_id_cards**](DefaultApi.md#get_members_id_cards) | **GET** /members/{id}/cards | Get Cards the Member is on
[**get_members_id_customboardbackgrounds**](DefaultApi.md#get_members_id_customboardbackgrounds) | **GET** /members/{id}/customBoardBackgrounds | Get a Member&#x27;s custom Board Backgrounds
[**get_members_id_customboardbackgrounds_idbackground**](DefaultApi.md#get_members_id_customboardbackgrounds_idbackground) | **GET** /members/{id}/customBoardBackgrounds/{idBackground} | Get custom Board Background of Member
[**get_members_id_customemoji**](DefaultApi.md#get_members_id_customemoji) | **GET** /members/{id}/customEmoji | Get a Member&#x27;s customEmojis
[**get_members_id_customstickers**](DefaultApi.md#get_members_id_customstickers) | **GET** /members/{id}/customStickers | Get Member&#x27;s custom Stickers
[**get_members_id_customstickers_idsticker**](DefaultApi.md#get_members_id_customstickers_idsticker) | **GET** /members/{id}/customStickers/{idSticker} | Get a Member&#x27;s custom Sticker
[**get_members_id_field**](DefaultApi.md#get_members_id_field) | **GET** /members/{id}/{field} | Get a field on a Member
[**get_members_id_notification_channel_settings**](DefaultApi.md#get_members_id_notification_channel_settings) | **GET** /members/{id}/notificationsChannelSettings | Get a Member&#x27;s notification channel settings
[**get_members_id_notification_channel_settings_channel**](DefaultApi.md#get_members_id_notification_channel_settings_channel) | **GET** /members/{id}/notificationsChannelSettings/{channel} | Get blocked notification keys of Member on this channel
[**get_members_id_notifications**](DefaultApi.md#get_members_id_notifications) | **GET** /members/{id}/notifications | Get Member&#x27;s Notifications
[**get_members_id_organizations**](DefaultApi.md#get_members_id_organizations) | **GET** /members/{id}/organizations | Get Member&#x27;s Organizations
[**get_members_id_organizationsinvited**](DefaultApi.md#get_members_id_organizationsinvited) | **GET** /members/{id}/organizationsInvited | Get Organizations a Member has been invited to
[**get_members_id_savedsearches**](DefaultApi.md#get_members_id_savedsearches) | **GET** /members/{id}/savedSearches | Get Member&#x27;s saved searched
[**get_members_id_savedsearches_idsearch**](DefaultApi.md#get_members_id_savedsearches_idsearch) | **GET** /members/{id}/savedSearches/{idSearch} | Get a saved search
[**get_members_id_tokens**](DefaultApi.md#get_members_id_tokens) | **GET** /members/{id}/tokens | Get Member&#x27;s Tokens
[**get_membersid**](DefaultApi.md#get_membersid) | **GET** /members/{id} | Get a Member
[**get_notifications_id**](DefaultApi.md#get_notifications_id) | **GET** /notifications/{id} | Get a Notification
[**get_notifications_id_board**](DefaultApi.md#get_notifications_id_board) | **GET** /notifications/{id}/board | Get the Board a Notification is on
[**get_notifications_id_card**](DefaultApi.md#get_notifications_id_card) | **GET** /notifications/{id}/card | Get the Card a Notification is on
[**get_notifications_id_field**](DefaultApi.md#get_notifications_id_field) | **GET** /notifications/{id}/{field} | Get a field of a Notification
[**get_notifications_id_list**](DefaultApi.md#get_notifications_id_list) | **GET** /notifications/{id}/list | Get the List a Notification is on
[**get_notifications_id_membercreator**](DefaultApi.md#get_notifications_id_membercreator) | **GET** /notifications/{id}/memberCreator | Get the Member who created the Notification
[**get_notifications_id_organization**](DefaultApi.md#get_notifications_id_organization) | **GET** /notifications/{id}/organization | Get a Notification&#x27;s associated Organization
[**get_organizations_id**](DefaultApi.md#get_organizations_id) | **GET** /organizations/{id} | Get an Organization
[**get_organizations_id_actions**](DefaultApi.md#get_organizations_id_actions) | **GET** /organizations/{id}/actions | Get Actions for Organization
[**get_organizations_id_boards**](DefaultApi.md#get_organizations_id_boards) | **GET** /organizations/{id}/boards | Get Boards in an Organization
[**get_organizations_id_exports**](DefaultApi.md#get_organizations_id_exports) | **GET** /organizations/{id}/exports | Retrieve Organization&#x27;s Exports
[**get_organizations_id_field**](DefaultApi.md#get_organizations_id_field) | **GET** /organizations/{id}/{field} | Get field on Organization
[**get_organizations_id_members**](DefaultApi.md#get_organizations_id_members) | **GET** /organizations/{id}/members | Get the Members of an Organization
[**get_organizations_id_memberships**](DefaultApi.md#get_organizations_id_memberships) | **GET** /organizations/{id}/memberships | Get Memberships of an Organization
[**get_organizations_id_memberships_idmembership**](DefaultApi.md#get_organizations_id_memberships_idmembership) | **GET** /organizations/{id}/memberships/{idMembership} | Get a Membership of an Organization
[**get_organizations_id_newbillableguests_idboard**](DefaultApi.md#get_organizations_id_newbillableguests_idboard) | **GET** /organizations/{id}/newBillableGuests/{idBoard} | Get Organizations new billable guests
[**get_organizations_id_plugindata**](DefaultApi.md#get_organizations_id_plugindata) | **GET** /organizations/{id}/pluginData | Get the pluginData Scoped to Organization
[**get_organizations_id_tags**](DefaultApi.md#get_organizations_id_tags) | **GET** /organizations/{id}/tags | Get Tags of an Organization
[**get_plugins_id**](DefaultApi.md#get_plugins_id) | **GET** /plugins/{id}/ | Get a Plugin
[**get_plugins_id_compliance_memberprivacy**](DefaultApi.md#get_plugins_id_compliance_memberprivacy) | **GET** /plugins/{id}/compliance/memberPrivacy | Get Plugin&#x27;s Member privacy compliance
[**get_search**](DefaultApi.md#get_search) | **GET** /search | Search Trello
[**get_search_members**](DefaultApi.md#get_search_members) | **GET** /search/members/ | Search for Members
[**get_tokens_token**](DefaultApi.md#get_tokens_token) | **GET** /tokens/{token} | Get a Token
[**get_tokens_token_member**](DefaultApi.md#get_tokens_token_member) | **GET** /tokens/{token}/member | Get Token&#x27;s Member
[**get_tokens_token_webhooks**](DefaultApi.md#get_tokens_token_webhooks) | **GET** /tokens/{token}/webhooks | Get Webhooks for Token
[**get_tokens_token_webhooks_idwebhook**](DefaultApi.md#get_tokens_token_webhooks_idwebhook) | **GET** /tokens/{token}/webhooks/{idWebhook} | Get a Webhook belonging to a Token
[**get_users_id**](DefaultApi.md#get_users_id) | **GET** /enterprises/{id}/members/query | Get Users of an Enterprise
[**get_webhooks_id**](DefaultApi.md#get_webhooks_id) | **GET** /webhooks/{id} | Get a Webhook
[**membersidavatar**](DefaultApi.md#membersidavatar) | **POST** /members/{id}/avatar | Create Avatar for Member
[**membersidcustomboardbackgrounds1**](DefaultApi.md#membersidcustomboardbackgrounds1) | **POST** /members/{id}/customBoardBackgrounds | Create a new custom Board Background
[**membersidcustomemojiidemoji**](DefaultApi.md#membersidcustomemojiidemoji) | **GET** /members/{id}/customEmoji/{idEmoji} | Get a Member&#x27;s custom Emoji
[**notificationsidmember**](DefaultApi.md#notificationsidmember) | **GET** /notifications/{id}/member | Get the Member a Notification is about (not the creator)
[**organizations_id_members_idmember_all**](DefaultApi.md#organizations_id_members_idmember_all) | **DELETE** /organizations/{id}/members/{idMember}/all | Remove a Member from an Organization and all Organization Boards
[**post_actions_idaction_reactions**](DefaultApi.md#post_actions_idaction_reactions) | **POST** /actions/{idAction}/reactions | Create Reaction for Action
[**post_boards**](DefaultApi.md#post_boards) | **POST** /boards/ | Create a Board
[**post_boards_id_boardplugins**](DefaultApi.md#post_boards_id_boardplugins) | **POST** /boards/{id}/boardPlugins | Enable a Power-Up on a Board
[**post_boards_id_calendarkey_generate**](DefaultApi.md#post_boards_id_calendarkey_generate) | **POST** /boards/{id}/calendarKey/generate | Create a calendarKey for a Board
[**post_boards_id_emailkey_generate**](DefaultApi.md#post_boards_id_emailkey_generate) | **POST** /boards/{id}/emailKey/generate | Create a emailKey for a Board
[**post_boards_id_idtags**](DefaultApi.md#post_boards_id_idtags) | **POST** /boards/{id}/idTags | Create a Tag for a Board
[**post_boards_id_labels**](DefaultApi.md#post_boards_id_labels) | **POST** /boards/{id}/labels | Create a Label on a Board
[**post_boards_id_lists**](DefaultApi.md#post_boards_id_lists) | **POST** /boards/{id}/lists | Create a List on a Board
[**post_boards_id_markedasviewed**](DefaultApi.md#post_boards_id_markedasviewed) | **POST** /boards/{id}/markedAsViewed | Mark Board as viewed
[**post_cards**](DefaultApi.md#post_cards) | **POST** /cards | Create a new Card
[**post_cards_id_actions_comments**](DefaultApi.md#post_cards_id_actions_comments) | **POST** /cards/{id}/actions/comments | Add a new comment to a Card
[**post_cards_id_attachments**](DefaultApi.md#post_cards_id_attachments) | **POST** /cards/{id}/attachments | Create Attachment On Card
[**post_cards_id_checklists**](DefaultApi.md#post_cards_id_checklists) | **POST** /cards/{id}/checklists | Create Checklist on a Card
[**post_cards_id_idlabels**](DefaultApi.md#post_cards_id_idlabels) | **POST** /cards/{id}/idLabels | Add a Label to a Card
[**post_cards_id_idmembers**](DefaultApi.md#post_cards_id_idmembers) | **POST** /cards/{id}/idMembers | Add a Member to a Card
[**post_cards_id_labels**](DefaultApi.md#post_cards_id_labels) | **POST** /cards/{id}/labels | Create a new Label on a Card
[**post_cards_id_markassociatednotificationsread**](DefaultApi.md#post_cards_id_markassociatednotificationsread) | **POST** /cards/{id}/markAssociatedNotificationsRead | Mark a Card&#x27;s Notifications as read
[**post_cards_id_stickers**](DefaultApi.md#post_cards_id_stickers) | **POST** /cards/{id}/stickers | Add a Sticker to a Card
[**post_checklists**](DefaultApi.md#post_checklists) | **POST** /checklists | Create a Checklist
[**post_checklists_id_checkitems**](DefaultApi.md#post_checklists_id_checkitems) | **POST** /checklists/{id}/checkItems | Create Checkitem on Checklist
[**post_customfields**](DefaultApi.md#post_customfields) | **POST** /customFields | Create a new Custom Field on a Board
[**post_customfields_id_options**](DefaultApi.md#post_customfields_id_options) | **GET** /customFields/{id}/options | Get Options of Custom Field drop down
[**post_enterprises_id_tokens**](DefaultApi.md#post_enterprises_id_tokens) | **POST** /enterprises/{id}/tokens | Create an auth Token for an Enterprise.
[**post_labels**](DefaultApi.md#post_labels) | **POST** /labels | Create a Label
[**post_lists**](DefaultApi.md#post_lists) | **POST** /lists | Create a new List
[**post_lists_id_archiveallcards**](DefaultApi.md#post_lists_id_archiveallcards) | **POST** /lists/{id}/archiveAllCards | Archive all Cards in List
[**post_lists_id_moveallcards**](DefaultApi.md#post_lists_id_moveallcards) | **POST** /lists/{id}/moveAllCards | Move all Cards in List
[**post_members_id_boardbackgrounds1**](DefaultApi.md#post_members_id_boardbackgrounds1) | **POST** /members/{id}/boardBackgrounds | Upload new boardBackground for Member
[**post_members_id_boardstars**](DefaultApi.md#post_members_id_boardstars) | **POST** /members/{id}/boardStars | Create Star for Board
[**post_members_id_customemoji**](DefaultApi.md#post_members_id_customemoji) | **POST** /members/{id}/customEmoji | Create custom Emoji for Member
[**post_members_id_customstickers**](DefaultApi.md#post_members_id_customstickers) | **POST** /members/{id}/customStickers | Create custom Sticker for Member
[**post_members_id_onetimemessagesdismissed**](DefaultApi.md#post_members_id_onetimemessagesdismissed) | **POST** /members/{id}/oneTimeMessagesDismissed | Dismiss a message for Member
[**post_members_id_savedsearches**](DefaultApi.md#post_members_id_savedsearches) | **POST** /members/{id}/savedSearches | Create saved Search for Member
[**post_notifications_all_read**](DefaultApi.md#post_notifications_all_read) | **POST** /notifications/all/read | Mark all Notifications as read
[**post_organizations**](DefaultApi.md#post_organizations) | **POST** /organizations | Create a new Organization
[**post_organizations_id_exports**](DefaultApi.md#post_organizations_id_exports) | **POST** /organizations/{id}/exports | Create Export for Organizations
[**post_organizations_id_logo**](DefaultApi.md#post_organizations_id_logo) | **POST** /organizations/{id}/logo | Update logo for an Organization
[**post_organizations_id_tags**](DefaultApi.md#post_organizations_id_tags) | **POST** /organizations/{id}/tags | Create a Tag in Organization
[**post_plugins_idplugin_listing**](DefaultApi.md#post_plugins_idplugin_listing) | **POST** /plugins/{idPlugin}/listing | Create a Listing for Plugin
[**post_tokens_token_webhooks**](DefaultApi.md#post_tokens_token_webhooks) | **POST** /tokens/{token}/webhooks | Create Webhooks for Token
[**post_webhooks**](DefaultApi.md#post_webhooks) | **POST** /webhooks/ | Create a Webhook
[**put_actions_id**](DefaultApi.md#put_actions_id) | **PUT** /actions/{id} | Update an Action
[**put_actions_id_text**](DefaultApi.md#put_actions_id_text) | **PUT** /actions/{id}/text | Update a Comment Action
[**put_boards_id**](DefaultApi.md#put_boards_id) | **PUT** /boards/{id} | Update a Board
[**put_boards_id_members**](DefaultApi.md#put_boards_id_members) | **PUT** /boards/{id}/members | Invite Member to Board via email
[**put_boards_id_members_idmember**](DefaultApi.md#put_boards_id_members_idmember) | **PUT** /boards/{id}/members/{idMember} | Add a Member to a Board
[**put_boards_id_memberships_idmembership**](DefaultApi.md#put_boards_id_memberships_idmembership) | **PUT** /boards/{id}/memberships/{idMembership} | Update Membership of Member on a Board
[**put_boards_id_my_prefs_showlistguide**](DefaultApi.md#put_boards_id_my_prefs_showlistguide) | **PUT** /boards/{id}/myPrefs/showListGuide | Update showListGuide Pref on a Board
[**put_boards_id_my_prefs_showsidebar**](DefaultApi.md#put_boards_id_my_prefs_showsidebar) | **PUT** /boards/{id}/myPrefs/showSidebar | Update showSidebar Pref on a Board
[**put_boards_id_my_prefs_showsidebaractivity**](DefaultApi.md#put_boards_id_my_prefs_showsidebaractivity) | **PUT** /boards/{id}/myPrefs/showSidebarActivity | Update showSidebarActivity Pref on a Board
[**put_boards_id_my_prefs_showsidebarboardactions**](DefaultApi.md#put_boards_id_my_prefs_showsidebarboardactions) | **PUT** /boards/{id}/myPrefs/showSidebarBoardActions | Update showSidebarBoardActions Pref on a Board
[**put_boards_id_my_prefs_showsidebarmembers**](DefaultApi.md#put_boards_id_my_prefs_showsidebarmembers) | **PUT** /boards/{id}/myPrefs/showSidebarMembers | Update showSidebarMembers Pref on a Board
[**put_boards_id_myprefs_emailposition**](DefaultApi.md#put_boards_id_myprefs_emailposition) | **PUT** /boards/{id}/myPrefs/emailPosition | Update emailPosition Pref on a Board
[**put_boards_id_myprefs_idemaillist**](DefaultApi.md#put_boards_id_myprefs_idemaillist) | **PUT** /boards/{id}/myPrefs/idEmailList | Update idEmailList Pref on a Board
[**put_cards_id**](DefaultApi.md#put_cards_id) | **PUT** /cards/{id} | Update a Card
[**put_cards_id_actions_idaction_comments**](DefaultApi.md#put_cards_id_actions_idaction_comments) | **PUT** /cards/{id}/actions/{idAction}/comments | Update Comment Action on a Card
[**put_cards_id_checkitem_idcheckitem**](DefaultApi.md#put_cards_id_checkitem_idcheckitem) | **PUT** /cards/{id}/checkItem/{idCheckItem} | Update a checkItem on a Card
[**put_cards_id_stickers_idsticker**](DefaultApi.md#put_cards_id_stickers_idsticker) | **PUT** /cards/{id}/stickers/{idSticker} | Update a Sticker on a Card
[**put_cards_idcard_checklist_idchecklist_checkitem_idcheckitem**](DefaultApi.md#put_cards_idcard_checklist_idchecklist_checkitem_idcheckitem) | **PUT** /cards/{idCard}/checklist/{idChecklist}/checkItem/{idCheckItem} | Update Checkitem on Checklist on Card
[**put_cards_idcard_customfield_idcustomfield_item**](DefaultApi.md#put_cards_idcard_customfield_idcustomfield_item) | **PUT** /cards/{idCard}/customField/{idCustomField}/item | Update Custom Field item on Card
[**put_cards_idcard_customfields**](DefaultApi.md#put_cards_idcard_customfields) | **PUT** /cards/{idCard}/customFields | Update Multiple Custom Field items on Card
[**put_checklists_id_field**](DefaultApi.md#put_checklists_id_field) | **PUT** /checklists/{id}/{field} | Update field on a Checklist
[**put_checlists_id**](DefaultApi.md#put_checlists_id) | **PUT** /checklists/{id} | Update a Checklist
[**put_customfields_id**](DefaultApi.md#put_customfields_id) | **PUT** /customFields/{id} | Update a Custom Field definition
[**put_enterprises_id_admins_idmember**](DefaultApi.md#put_enterprises_id_admins_idmember) | **PUT** /enterprises/{id}/admins/{idMember} | Update Member to be admin of Enterprise
[**put_enterprises_id_enterprise_join_request_bulk**](DefaultApi.md#put_enterprises_id_enterprise_join_request_bulk) | **PUT** /enterprises/${id}/enterpriseJoinRequest/bulk | Decline enterpriseJoinRequests from one organization or a bulk list of organizations.
[**put_enterprises_id_members_idmember_licensed**](DefaultApi.md#put_enterprises_id_members_idmember_licensed) | **PUT** /enterprises/{id}/members/{idMember}/licensed | Update a Member&#x27;s licensed status
[**put_enterprises_id_organizations**](DefaultApi.md#put_enterprises_id_organizations) | **PUT** /enterprises/{id}/organizations | Transfer an Organization to an Enterprise.
[**put_id_idboard**](DefaultApi.md#put_id_idboard) | **PUT** /lists/{id}/idBoard | Move List to Board
[**put_labels_id**](DefaultApi.md#put_labels_id) | **PUT** /labels/{id} | Update a Label
[**put_labels_id_field**](DefaultApi.md#put_labels_id_field) | **PUT** /labels/{id}/{field} | Update a field on a label
[**put_lists_id**](DefaultApi.md#put_lists_id) | **PUT** /lists/{id} | Update a List
[**put_lists_id_closed**](DefaultApi.md#put_lists_id_closed) | **PUT** /lists/{id}/closed | Archive or unarchive a list
[**put_lists_id_field**](DefaultApi.md#put_lists_id_field) | **PUT** /lists/{id}/{field} | Update a field on a List
[**put_members_id**](DefaultApi.md#put_members_id) | **PUT** /members/{id} | Update a Member
[**put_members_id_boardbackgrounds_idbackground**](DefaultApi.md#put_members_id_boardbackgrounds_idbackground) | **PUT** /members/{id}/boardBackgrounds/{idBackground} | Update a Member&#x27;s custom Board background
[**put_members_id_boardstars_idstar**](DefaultApi.md#put_members_id_boardstars_idstar) | **PUT** /members/{id}/boardStars/{idStar} | Update the position of a boardStar of Member
[**put_members_id_customboardbackgrounds_idbackground**](DefaultApi.md#put_members_id_customboardbackgrounds_idbackground) | **PUT** /members/{id}/customBoardBackgrounds/{idBackground} | Update custom Board Background of Member
[**put_members_id_notification_channel_settings_channel_blocked_keys**](DefaultApi.md#put_members_id_notification_channel_settings_channel_blocked_keys) | **PUT** /members/{id}/notificationsChannelSettings | Update blocked notification keys of Member on a channel
[**put_members_id_notification_channel_settings_channel_blocked_keys_0**](DefaultApi.md#put_members_id_notification_channel_settings_channel_blocked_keys_0) | **PUT** /members/{id}/notificationsChannelSettings/{channel} | Update blocked notification keys of Member on a channel
[**put_members_id_notification_channel_settings_channel_blocked_keys_1**](DefaultApi.md#put_members_id_notification_channel_settings_channel_blocked_keys_1) | **PUT** /members/{id}/notificationsChannelSettings/{channel}/{blockedKeys} | Update blocked notification keys of Member on a channel
[**put_members_id_savedsearches_idsearch**](DefaultApi.md#put_members_id_savedsearches_idsearch) | **PUT** /members/{id}/savedSearches/{idSearch} | Update a saved search
[**put_notifications_id**](DefaultApi.md#put_notifications_id) | **PUT** /notifications/{id} | Update a Notification&#x27;s read status
[**put_notifications_id_unread**](DefaultApi.md#put_notifications_id_unread) | **PUT** /notifications/{id}/unread | Update Notification&#x27;s read status
[**put_organizations_id**](DefaultApi.md#put_organizations_id) | **PUT** /organizations/{id} | Update an Organization
[**put_organizations_id_members**](DefaultApi.md#put_organizations_id_members) | **PUT** /organizations/{id}/members | Update an Organization&#x27;s Members
[**put_organizations_id_members_idmember**](DefaultApi.md#put_organizations_id_members_idmember) | **PUT** /organizations/{id}/members/{idMember} | Update a Member of an Organization
[**put_organizations_id_members_idmember_deactivated**](DefaultApi.md#put_organizations_id_members_idmember_deactivated) | **PUT** /organizations/{id}/members/{idMember}/deactivated | Deactivate or reactivate a member of an Organization
[**put_plugins_id**](DefaultApi.md#put_plugins_id) | **PUT** /plugins/{id}/ | Update a Plugin
[**put_plugins_idplugin_listings_idlisting**](DefaultApi.md#put_plugins_idplugin_listings_idlisting) | **PUT** /plugins/{idPlugin}/listings/{idListing} | Updating Plugin&#x27;s Listing
[**put_webhooks_id**](DefaultApi.md#put_webhooks_id) | **PUT** /webhooks/{id} | Update a Webhook
[**tokenstokenwebhooks1**](DefaultApi.md#tokenstokenwebhooks1) | **PUT** /tokens/{token}/webhooks/{idWebhook} | Update a Webhook created by Token
[**webhooksidfield**](DefaultApi.md#webhooksidfield) | **GET** /webhooks/{id}/{field} | Get a field on a Webhook

# **applications_key_compliance**
> applications_key_compliance(key)

Get Application's compliance data

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
key = 'key_example' # str | 

try:
    # Get Application's compliance data
    api_instance.applications_key_compliance(key)
except ApiException as e:
    print("Exception when calling DefaultApi->applications_key_compliance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boards_id_checklists**
> boards_id_checklists(id)

Get Checklists on a Board

Get all of the checklists on a Board.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the board

try:
    # Get Checklists on a Board
    api_instance.boards_id_checklists(id)
except ApiException as e:
    print("Exception when calling DefaultApi->boards_id_checklists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the board | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **boardsidmembersidmember**
> boardsidmembersidmember(id, id_member)

Remove Member from Board

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The id of the board to update
id_member = trello_api_client.TrelloID() # TrelloID | The id of the member to add to the board.

try:
    # Remove Member from Board
    api_instance.boardsidmembersidmember(id, id_member)
except ApiException as e:
    print("Exception when calling DefaultApi->boardsidmembersidmember: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The id of the board to update | 
 **id_member** | [**TrelloID**](.md)| The id of the member to add to the board. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cardsidmembersvoted1**
> cardsidmembersvoted1(id, value)

Add Member vote to Card

Vote on the card for a given member.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
value = trello_api_client.TrelloID() # TrelloID | The ID of the member to vote 'yes' on the card

try:
    # Add Member vote to Card
    api_instance.cardsidmembersvoted1(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->cardsidmembersvoted1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **value** | [**TrelloID**](.md)| The ID of the member to vote &#x27;yes&#x27; on the card | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_actions_id**
> delete_actions_id(id)

Delete an Action

Delete a specific action. Only comment actions can be deleted.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Action

try:
    # Delete an Action
    api_instance.delete_actions_id(id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_actions_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Action | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_actions_idaction_reactions_id**
> delete_actions_idaction_reactions_id(id_action, id)

Delete Action's Reaction

Deletes a reaction

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id_action = trello_api_client.TrelloID() # TrelloID | The ID of the Action
id = trello_api_client.TrelloID() # TrelloID | The ID of the reaction

try:
    # Delete Action's Reaction
    api_instance.delete_actions_idaction_reactions_id(id_action, id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_actions_idaction_reactions_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_action** | [**TrelloID**](.md)| The ID of the Action | 
 **id** | [**TrelloID**](.md)| The ID of the reaction | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_boards_id**
> delete_boards_id(id)

Delete a Board

Delete a board.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the board to delete

try:
    # Delete a Board
    api_instance.delete_boards_id(id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_boards_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the board to delete | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_boards_id_boardplugins**
> delete_boards_id_boardplugins(id, id_plugin)

Disable a Power-Up on a Board

Disable a Power-Up on a board

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the board
id_plugin = trello_api_client.TrelloID() # TrelloID | The ID of the Power-Up to disable

try:
    # Disable a Power-Up on a Board
    api_instance.delete_boards_id_boardplugins(id, id_plugin)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_boards_id_boardplugins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the board | 
 **id_plugin** | [**TrelloID**](.md)| The ID of the Power-Up to disable | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cards_id**
> delete_cards_id(id)

Delete a Card

Delete a Card

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card

try:
    # Delete a Card
    api_instance.delete_cards_id(id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_cards_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cards_id_actions_id_comments**
> delete_cards_id_actions_id_comments(id, id_action)

Delete a comment on a Card

Delete a comment

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
id_action = trello_api_client.TrelloID() # TrelloID | The ID of the comment action to update

try:
    # Delete a comment on a Card
    api_instance.delete_cards_id_actions_id_comments(id, id_action)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_cards_id_actions_id_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **id_action** | [**TrelloID**](.md)| The ID of the comment action to update | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cards_id_checkitem_idcheckitem**
> delete_cards_id_checkitem_idcheckitem(id, id_check_item)

Delete checkItem on a Card

Delete a checklist item

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
id_check_item = trello_api_client.TrelloID() # TrelloID | The ID of the checkitem

try:
    # Delete checkItem on a Card
    api_instance.delete_cards_id_checkitem_idcheckitem(id, id_check_item)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_cards_id_checkitem_idcheckitem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **id_check_item** | [**TrelloID**](.md)| The ID of the checkitem | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cards_id_checklists_idchecklist**
> delete_cards_id_checklists_idchecklist(id, id_checklist)

Delete a Checklist on a Card

Delete a checklist from a card

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
id_checklist = trello_api_client.TrelloID() # TrelloID | The ID of the checklist to delete

try:
    # Delete a Checklist on a Card
    api_instance.delete_cards_id_checklists_idchecklist(id, id_checklist)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_cards_id_checklists_idchecklist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **id_checklist** | [**TrelloID**](.md)| The ID of the checklist to delete | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cards_id_idlabels_idlabel**
> delete_cards_id_idlabels_idlabel(id, id_label)

Remove a Label from a Card

Remove a label from a card

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
id_label = trello_api_client.TrelloID() # TrelloID | The ID of the label to remove

try:
    # Remove a Label from a Card
    api_instance.delete_cards_id_idlabels_idlabel(id, id_label)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_cards_id_idlabels_idlabel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **id_label** | [**TrelloID**](.md)| The ID of the label to remove | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cards_id_membersvoted_idmember**
> delete_cards_id_membersvoted_idmember(id, id_member)

Remove a Member's Vote on a Card

Remove a member's vote from a card

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
id_member = trello_api_client.TrelloID() # TrelloID | The ID of the member whose vote to remove

try:
    # Remove a Member's Vote on a Card
    api_instance.delete_cards_id_membersvoted_idmember(id, id_member)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_cards_id_membersvoted_idmember: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **id_member** | [**TrelloID**](.md)| The ID of the member whose vote to remove | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cards_id_stickers_idsticker**
> delete_cards_id_stickers_idsticker(id, id_sticker)

Delete a Sticker on a Card

Remove a sticker from the card

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
id_sticker = trello_api_client.TrelloID() # TrelloID | The ID of the sticker

try:
    # Delete a Sticker on a Card
    api_instance.delete_cards_id_stickers_idsticker(id, id_sticker)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_cards_id_stickers_idsticker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **id_sticker** | [**TrelloID**](.md)| The ID of the sticker | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_checklists_id**
> delete_checklists_id(id)

Delete a Checklist

Delete a checklist

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of a checklist.

try:
    # Delete a Checklist
    api_instance.delete_checklists_id(id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_checklists_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of a checklist. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_checklists_id_checkitems_idcheckitem**
> delete_checklists_id_checkitems_idcheckitem(id, id_check_item)

Delete Checkitem from Checklist

Remove an item from a checklist

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of a checklist.
id_check_item = trello_api_client.TrelloID() # TrelloID | ID of the check item to retrieve.

try:
    # Delete Checkitem from Checklist
    api_instance.delete_checklists_id_checkitems_idcheckitem(id, id_check_item)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_checklists_id_checkitems_idcheckitem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of a checklist. | 
 **id_check_item** | [**TrelloID**](.md)| ID of the check item to retrieve. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customfields_id**
> delete_customfields_id(id)

Delete a Custom Field definition

Delete a Custom Field from a board.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the Custom Field.

try:
    # Delete a Custom Field definition
    api_instance.delete_customfields_id(id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_customfields_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the Custom Field. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customfields_options_idcustomfieldoption**
> delete_customfields_options_idcustomfieldoption(id, id_custom_field_option)

Delete Option of Custom Field dropdown

Delete an option from a Custom Field dropdown.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the customfielditem.
id_custom_field_option = trello_api_client.TrelloID() # TrelloID | ID of the customfieldoption to retrieve.

try:
    # Delete Option of Custom Field dropdown
    api_instance.delete_customfields_options_idcustomfieldoption(id, id_custom_field_option)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_customfields_options_idcustomfieldoption: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the customfielditem. | 
 **id_custom_field_option** | [**TrelloID**](.md)| ID of the customfieldoption to retrieve. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_enterprises_id_organizations_idorg**
> delete_enterprises_id_organizations_idorg(id, id_org)

Delete an Organization from an Enterprise.

Remove an organization from an enterprise.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the enterprise to retrieve.
id_org = trello_api_client.TrelloID() # TrelloID | ID of the organization to be removed from the enterprise.

try:
    # Delete an Organization from an Enterprise.
    api_instance.delete_enterprises_id_organizations_idorg(id, id_org)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_enterprises_id_organizations_idorg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the enterprise to retrieve. | 
 **id_org** | [**TrelloID**](.md)| ID of the organization to be removed from the enterprise. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_id_idmembers_idmember**
> delete_id_idmembers_idmember(id, id_member)

Remove a Member from a Card

Remove a member from a card

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
id_member = trello_api_client.TrelloID() # TrelloID | The ID of the member to remove from the card

try:
    # Remove a Member from a Card
    api_instance.delete_id_idmembers_idmember(id, id_member)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_id_idmembers_idmember: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **id_member** | [**TrelloID**](.md)| The ID of the member to remove from the card | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_labels_id**
> delete_labels_id(id)

Delete a Label

Delete a label by ID.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Label

try:
    # Delete a Label
    api_instance.delete_labels_id(id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_labels_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Label | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_members_id_boardbackgrounds_idbackground**
> delete_members_id_boardbackgrounds_idbackground(id, id_background)

Delete a Member's custom Board background

Delete a board background

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member
id_background = trello_api_client.TrelloID() # TrelloID | The ID of the board background

try:
    # Delete a Member's custom Board background
    api_instance.delete_members_id_boardbackgrounds_idbackground(id, id_background)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_members_id_boardbackgrounds_idbackground: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 
 **id_background** | [**TrelloID**](.md)| The ID of the board background | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_members_id_boardstars_idstar**
> delete_members_id_boardstars_idstar(id, id_star)

Delete Star for Board

Unstar a board

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member
id_star = trello_api_client.TrelloID() # TrelloID | The ID of the board star

try:
    # Delete Star for Board
    api_instance.delete_members_id_boardstars_idstar(id, id_star)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_members_id_boardstars_idstar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 
 **id_star** | [**TrelloID**](.md)| The ID of the board star | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_members_id_customboardbackgrounds_idbackground**
> delete_members_id_customboardbackgrounds_idbackground(id, id_background)

Delete custom Board Background of Member

Delete a specific custom board background

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.Id2() # Id2 | The ID or username of the member
id_background = trello_api_client.TrelloID() # TrelloID | The ID of the custom background

try:
    # Delete custom Board Background of Member
    api_instance.delete_members_id_customboardbackgrounds_idbackground(id, id_background)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_members_id_customboardbackgrounds_idbackground: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id2**](.md)| The ID or username of the member | 
 **id_background** | [**TrelloID**](.md)| The ID of the custom background | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_members_id_customstickers_idsticker**
> delete_members_id_customstickers_idsticker(id, id_sticker)

Delete a Member's custom Sticker

Delete a Member's custom Sticker

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member
id_sticker = trello_api_client.TrelloID() # TrelloID | The ID of the uploaded sticker

try:
    # Delete a Member's custom Sticker
    api_instance.delete_members_id_customstickers_idsticker(id, id_sticker)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_members_id_customstickers_idsticker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 
 **id_sticker** | [**TrelloID**](.md)| The ID of the uploaded sticker | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_members_id_savedsearches_idsearch**
> delete_members_id_savedsearches_idsearch(id, id_search)

Delete a saved search

Delete a saved search

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
id_search = 'id_search_example' # str | The ID of the saved search to delete

try:
    # Delete a saved search
    api_instance.delete_members_id_savedsearches_idsearch(id, id_search)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_members_id_savedsearches_idsearch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **id_search** | **str**| The ID of the saved search to delete | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organizations_id**
> delete_organizations_id(id)

Delete an Organization

Delete an Organization

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or name of the Organization

try:
    # Delete an Organization
    api_instance.delete_organizations_id(id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_organizations_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or name of the Organization | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organizations_id_logo**
> delete_organizations_id_logo(id)

Delete Logo for Organization

Delete a the logo from a Workspace

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or name of the organization

try:
    # Delete Logo for Organization
    api_instance.delete_organizations_id_logo(id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_organizations_id_logo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or name of the organization | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organizations_id_members**
> delete_organizations_id_members(id, id_member)

Remove a Member from an Organization

Remove a member from a Workspace

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.Id7() # Id7 | The ID or name of the organization
id_member = trello_api_client.TrelloID() # TrelloID | The ID of the Member to remove from the Workspace

try:
    # Remove a Member from an Organization
    api_instance.delete_organizations_id_members(id, id_member)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_organizations_id_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id7**](.md)| The ID or name of the organization | 
 **id_member** | [**TrelloID**](.md)| The ID of the Member to remove from the Workspace | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organizations_id_prefs_associateddomain**
> delete_organizations_id_prefs_associateddomain(id)

Remove the associated Google Apps domain from a Workspace

Remove the associated Google Apps domain from a Workspace

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or name of the organization

try:
    # Remove the associated Google Apps domain from a Workspace
    api_instance.delete_organizations_id_prefs_associateddomain(id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_organizations_id_prefs_associateddomain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or name of the organization | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organizations_id_prefs_orginviterestrict**
> delete_organizations_id_prefs_orginviterestrict(id)

Delete the email domain restriction on who can be invited to the Workspace

Remove the email domain restriction on who can be invited to the Workspace

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or name of the organization

try:
    # Delete the email domain restriction on who can be invited to the Workspace
    api_instance.delete_organizations_id_prefs_orginviterestrict(id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_organizations_id_prefs_orginviterestrict: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or name of the organization | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organizations_id_tags_idtag**
> delete_organizations_id_tags_idtag(id, id_tag)

Delete an Organization's Tag

Delete an organization's tag

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = 'id_example' # str | The ID or name of the organization
id_tag = 'id_tag_example' # str | The ID of the tag to delete

try:
    # Delete an Organization's Tag
    api_instance.delete_organizations_id_tags_idtag(id, id_tag)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_organizations_id_tags_idtag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or name of the organization | 
 **id_tag** | **str**| The ID of the tag to delete | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token**
> delete_token(token)

Delete a Token

Delete a token.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
token = 'token_example' # str | 

try:
    # Delete a Token
    api_instance.delete_token(token)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tokens_token_webhooks_idwebhook**
> delete_tokens_token_webhooks_idwebhook(token, id_webhook)

Delete a Webhook created by Token

Delete a webhook created with given token.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
token = 'token_example' # str | 
id_webhook = trello_api_client.TrelloID() # TrelloID | ID of the [Webhooks](ref:webhooks) to retrieve.

try:
    # Delete a Webhook created by Token
    api_instance.delete_tokens_token_webhooks_idwebhook(token, id_webhook)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_tokens_token_webhooks_idwebhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **id_webhook** | [**TrelloID**](.md)| ID of the [Webhooks](ref:webhooks) to retrieve. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhooks_id**
> delete_webhooks_id(id)

Delete a Webhook

Delete a webhook by ID.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the webhook to retrieve.

try:
    # Delete a Webhook
    api_instance.delete_webhooks_id(id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_webhooks_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the webhook to retrieve. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deleted_cards_id_attachments_idattachment**
> deleted_cards_id_attachments_idattachment(id, id_attachment)

Delete an Attachment on a Card

Delete an Attachment

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
id_attachment = trello_api_client.TrelloID() # TrelloID | The ID of the attachment to delete

try:
    # Delete an Attachment on a Card
    api_instance.deleted_cards_id_attachments_idattachment(id, id_attachment)
except ApiException as e:
    print("Exception when calling DefaultApi->deleted_cards_id_attachments_idattachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **id_attachment** | [**TrelloID**](.md)| The ID of the attachment to delete | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **emoji**
> Emoji emoji(locale=locale, spritesheets=spritesheets)

List available Emoji

List available Emoji

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = trello_api_client.DefaultApi()
locale = 'locale_example' # str | The locale to return emoji descriptions and names in. Defaults to the logged in member's locale. (optional)
spritesheets = false # bool | `true` to return spritesheet URLs in the response (optional) (default to false)

try:
    # List available Emoji
    api_response = api_instance.emoji(locale=locale, spritesheets=spritesheets)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->emoji: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | **str**| The locale to return emoji descriptions and names in. Defaults to the logged in member&#x27;s locale. | [optional] 
 **spritesheets** | **bool**| &#x60;true&#x60; to return spritesheet URLs in the response | [optional] [default to false]

### Return type

[**Emoji**](Emoji.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_id_members_id_member_deactivated**
> enterprises_id_members_id_member_deactivated(id, id_member, value, fields=fields, organization_fields=organization_fields, board_fields=board_fields)

Deactivate a Member of an Enterprise.

Deactivate a Member of an Enterprise.   NOTE: Deactivation is not possible for enterprises that have opted in to user management via AdminHub.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the enterprise to retrieve.
id_member = trello_api_client.TrelloID() # TrelloID | ID of the Member to deactive.
value = true # bool | Determines whether the user is deactivated or not.
fields = trello_api_client.MemberFields() # MemberFields | A comma separated list of any valid values that the [nested member field resource]() accepts. (optional)
organization_fields = trello_api_client.OrganizationFields() # OrganizationFields | Any valid value that the [nested organization resource](/cloud/trello/guides/rest-api/nested-resources/) accepts. (optional)
board_fields = trello_api_client.BoardFields() # BoardFields | Any valid value that the [nested board resource](/cloud/trello/guides/rest-api/nested-resources/) accepts. (optional)

try:
    # Deactivate a Member of an Enterprise.
    api_instance.enterprises_id_members_id_member_deactivated(id, id_member, value, fields=fields, organization_fields=organization_fields, board_fields=board_fields)
except ApiException as e:
    print("Exception when calling DefaultApi->enterprises_id_members_id_member_deactivated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the enterprise to retrieve. | 
 **id_member** | [**TrelloID**](.md)| ID of the Member to deactive. | 
 **value** | **bool**| Determines whether the user is deactivated or not. | 
 **fields** | [**MemberFields**](.md)| A comma separated list of any valid values that the [nested member field resource]() accepts. | [optional] 
 **organization_fields** | [**OrganizationFields**](.md)| Any valid value that the [nested organization resource](/cloud/trello/guides/rest-api/nested-resources/) accepts. | [optional] 
 **board_fields** | [**BoardFields**](.md)| Any valid value that the [nested board resource](/cloud/trello/guides/rest-api/nested-resources/) accepts. | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enterprises_id_organizations_idmember**
> enterprises_id_organizations_idmember(id, id_member)

Remove a Member as admin from Enterprise.

Remove a member as admin from an enterprise.   NOTE: This endpoint is not available to enterprises that have opted in to user management via AdminHub.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the Enterprise to retrieve.
id_member = trello_api_client.TrelloID() # TrelloID | ID of the member to be removed as an admin from enterprise.

try:
    # Remove a Member as admin from Enterprise.
    api_instance.enterprises_id_organizations_idmember(id, id_member)
except ApiException as e:
    print("Exception when calling DefaultApi->enterprises_id_organizations_idmember: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the Enterprise to retrieve. | 
 **id_member** | [**TrelloID**](.md)| ID of the member to be removed as an admin from enterprise. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_actions_id**
> get_actions_id(id, display=display, entities=entities, fields=fields, member=member, member_fields=member_fields, member_creator=member_creator, member_creator_fields=member_creator_fields)

Get an Action

Get an Action

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Action
display = true # bool |  (optional) (default to true)
entities = false # bool |  (optional) (default to false)
fields = 'all' # str | `all` or a comma-separated list of action [fields](/cloud/trello/guides/rest-api/object-definitions/#action-object) (optional) (default to all)
member = true # bool |  (optional) (default to true)
member_fields = 'avatarHash,fullName,initials,username' # str | `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional) (default to avatarHash,fullName,initials,username)
member_creator = true # bool | Whether to include the member object for the creator of the action (optional) (default to true)
member_creator_fields = 'avatarHash,fullName,initials,username' # str | `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional) (default to avatarHash,fullName,initials,username)

try:
    # Get an Action
    api_instance.get_actions_id(id, display=display, entities=entities, fields=fields, member=member, member_fields=member_fields, member_creator=member_creator, member_creator_fields=member_creator_fields)
except ApiException as e:
    print("Exception when calling DefaultApi->get_actions_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Action | 
 **display** | **bool**|  | [optional] [default to true]
 **entities** | **bool**|  | [optional] [default to false]
 **fields** | **str**| &#x60;all&#x60; or a comma-separated list of action [fields](/cloud/trello/guides/rest-api/object-definitions/#action-object) | [optional] [default to all]
 **member** | **bool**|  | [optional] [default to true]
 **member_fields** | **str**| &#x60;all&#x60; or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] [default to avatarHash,fullName,initials,username]
 **member_creator** | **bool**| Whether to include the member object for the creator of the action | [optional] [default to true]
 **member_creator_fields** | **str**| &#x60;all&#x60; or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] [default to avatarHash,fullName,initials,username]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_actions_id_board**
> Board get_actions_id_board(id, fields=fields)

Get the Board for an Action

Get the Board for an Action

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the action
fields = trello_api_client.BoardFields() # BoardFields | `all` or a comma-separated list of board fields (optional)

try:
    # Get the Board for an Action
    api_response = api_instance.get_actions_id_board(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_actions_id_board: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the action | 
 **fields** | [**BoardFields**](.md)| &#x60;all&#x60; or a comma-separated list of board fields | [optional] 

### Return type

[**Board**](Board.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_actions_id_card**
> Card get_actions_id_card(id, fields=fields)

Get the Card for an Action

Get the card for an action

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the action
fields = trello_api_client.CardFields() # CardFields | `all` or a comma-separated list of card fields (optional)

try:
    # Get the Card for an Action
    api_response = api_instance.get_actions_id_card(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_actions_id_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the action | 
 **fields** | [**CardFields**](.md)| &#x60;all&#x60; or a comma-separated list of card fields | [optional] 

### Return type

[**Card**](Card.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_actions_id_field**
> Action get_actions_id_field(id, field)

Get a specific field on an Action

Get a specific property of an action

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Action
field = trello_api_client.ActionFields() # ActionFields | An action field

try:
    # Get a specific field on an Action
    api_response = api_instance.get_actions_id_field(id, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_actions_id_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Action | 
 **field** | [**ActionFields**](.md)| An action field | 

### Return type

[**Action**](Action.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_actions_id_list**
> TrelloList get_actions_id_list(id, fields=fields)

Get the List for an Action

Get the List for an Action

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the action
fields = trello_api_client.ListFields() # ListFields | `all` or a comma-separated list of list fields (optional)

try:
    # Get the List for an Action
    api_response = api_instance.get_actions_id_list(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_actions_id_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the action | 
 **fields** | [**ListFields**](.md)| &#x60;all&#x60; or a comma-separated list of list fields | [optional] 

### Return type

[**TrelloList**](TrelloList.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_actions_id_member**
> Member get_actions_id_member(id, fields=fields)

Get the Member of an Action

Gets the member of an action (not the creator)

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Action
fields = trello_api_client.MemberFields() # MemberFields | `all` or a comma-separated list of member fields (optional)

try:
    # Get the Member of an Action
    api_response = api_instance.get_actions_id_member(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_actions_id_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Action | 
 **fields** | [**MemberFields**](.md)| &#x60;all&#x60; or a comma-separated list of member fields | [optional] 

### Return type

[**Member**](Member.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_actions_id_membercreator**
> Member get_actions_id_membercreator(id, fields=fields)

Get the Member Creator of an Action

Get the Member who created the Action

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Action
fields = trello_api_client.MemberFields() # MemberFields | `all` or a comma-separated list of member fields (optional)

try:
    # Get the Member Creator of an Action
    api_response = api_instance.get_actions_id_membercreator(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_actions_id_membercreator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Action | 
 **fields** | [**MemberFields**](.md)| &#x60;all&#x60; or a comma-separated list of member fields | [optional] 

### Return type

[**Member**](Member.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_actions_id_organization**
> Organization get_actions_id_organization(id, fields=fields)

Get the Organization of an Action

Get the Organization of an Action

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the action
fields = trello_api_client.OrganizationFields() # OrganizationFields | `all` or a comma-separated list of organization fields (optional)

try:
    # Get the Organization of an Action
    api_response = api_instance.get_actions_id_organization(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_actions_id_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the action | 
 **fields** | [**OrganizationFields**](.md)| &#x60;all&#x60; or a comma-separated list of organization fields | [optional] 

### Return type

[**Organization**](Organization.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_actions_idaction_reactions**
> get_actions_idaction_reactions(id_action, member=member, emoji=emoji)

Get Action's Reactions

List reactions for an action

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id_action = trello_api_client.TrelloID() # TrelloID | The ID of the action
member = true # bool | Whether to load the member as a nested resource. See [Members Nested Resource](/cloud/trello/guides/rest-api/nested-resources/#members-nested-resource) (optional) (default to true)
emoji = true # bool | Whether to load the emoji as a nested resource. (optional) (default to true)

try:
    # Get Action's Reactions
    api_instance.get_actions_idaction_reactions(id_action, member=member, emoji=emoji)
except ApiException as e:
    print("Exception when calling DefaultApi->get_actions_idaction_reactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_action** | [**TrelloID**](.md)| The ID of the action | 
 **member** | **bool**| Whether to load the member as a nested resource. See [Members Nested Resource](/cloud/trello/guides/rest-api/nested-resources/#members-nested-resource) | [optional] [default to true]
 **emoji** | **bool**| Whether to load the emoji as a nested resource. | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_actions_idaction_reactions_id**
> get_actions_idaction_reactions_id(id_action, id, member=member, emoji=emoji)

Get Action's Reaction

Get information for a reaction

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id_action = trello_api_client.TrelloID() # TrelloID | The ID of the Action
id = trello_api_client.TrelloID() # TrelloID | The ID of the reaction
member = true # bool | Whether to load the member as a nested resource. See [Members Nested Resource](/cloud/trello/guides/rest-api/nested-resources/#members-nested-resource) (optional) (default to true)
emoji = true # bool | Whether to load the emoji as a nested resource. (optional) (default to true)

try:
    # Get Action's Reaction
    api_instance.get_actions_idaction_reactions_id(id_action, id, member=member, emoji=emoji)
except ApiException as e:
    print("Exception when calling DefaultApi->get_actions_idaction_reactions_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_action** | [**TrelloID**](.md)| The ID of the Action | 
 **id** | [**TrelloID**](.md)| The ID of the reaction | 
 **member** | **bool**| Whether to load the member as a nested resource. See [Members Nested Resource](/cloud/trello/guides/rest-api/nested-resources/#members-nested-resource) | [optional] [default to true]
 **emoji** | **bool**| Whether to load the emoji as a nested resource. | [optional] [default to true]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_actions_idaction_reactionsummary**
> get_actions_idaction_reactionsummary(id_action)

List Action's summary of Reactions

List a summary of all reactions for an action

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id_action = trello_api_client.TrelloID() # TrelloID | The ID of the action

try:
    # List Action's summary of Reactions
    api_instance.get_actions_idaction_reactionsummary(id_action)
except ApiException as e:
    print("Exception when calling DefaultApi->get_actions_idaction_reactionsummary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_action** | [**TrelloID**](.md)| The ID of the action | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_batch**
> get_batch(urls)

Batch Requests

Make up to 10 GET requests in a single, batched API call.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
urls = 'urls_example' # str | A list of API routes. Maximum of 10 routes allowed. The routes should begin with a forward slash and should not include the API version number - e.g. \"urls=/members/trello,/cards/[cardId]\"

try:
    # Batch Requests
    api_instance.get_batch(urls)
except ApiException as e:
    print("Exception when calling DefaultApi->get_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **urls** | **str**| A list of API routes. Maximum of 10 routes allowed. The routes should begin with a forward slash and should not include the API version number - e.g. \&quot;urls&#x3D;/members/trello,/cards/[cardId]\&quot; | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_board_id_plugins**
> Plugin get_board_id_plugins(id, filter=filter)

Get Power-Ups on a Board

List the Power-Ups on a board

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the board
filter = 'enabled' # str | One of: `enabled` or `available` (optional) (default to enabled)

try:
    # Get Power-Ups on a Board
    api_response = api_instance.get_board_id_plugins(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_board_id_plugins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the board | 
 **filter** | **str**| One of: &#x60;enabled&#x60; or &#x60;available&#x60; | [optional] [default to enabled]

### Return type

[**Plugin**](Plugin.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_boards_id**
> Board get_boards_id(id, actions=actions, board_stars=board_stars, cards=cards, card_plugin_data=card_plugin_data, checklists=checklists, custom_fields=custom_fields, fields=fields, labels=labels, lists=lists, members=members, memberships=memberships, plugin_data=plugin_data, organization=organization, organization_plugin_data=organization_plugin_data, my_prefs=my_prefs, tags=tags)

Get a Board

Request a single board.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | 
actions = 'all' # str | This is a nested resource. Read more about actions as nested resources [here](/cloud/trello/guides/rest-api/nested-resources/). (optional) (default to all)
board_stars = 'none' # str | Valid values are one of: `mine` or `none`. (optional) (default to none)
cards = 'none' # str | This is a nested resource. Read more about cards as nested resources [here](/cloud/trello/guides/rest-api/nested-resources/). (optional) (default to none)
card_plugin_data = false # bool | Use with the `cards` param to include card pluginData with the response (optional) (default to false)
checklists = 'none' # str | This is a nested resource. Read more about checklists as nested resources [here](/cloud/trello/guides/rest-api/nested-resources/). (optional) (default to none)
custom_fields = false # bool | This is a nested resource. Read more about custom fields as nested resources [here](#custom-fields-nested-resource). (optional) (default to false)
fields = 'name,desc,descData,closed,idOrganization,pinned,url,shortUrl,prefs,labelNames' # str | The fields of the board to be included in the response. Valid values: all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idMemberCreator, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed, url (optional) (default to name,desc,descData,closed,idOrganization,pinned,url,shortUrl,prefs,labelNames)
labels = 'labels_example' # str | This is a nested resource. Read more about labels as nested resources [here](/cloud/trello/guides/rest-api/nested-resources/). (optional)
lists = 'open' # str | This is a nested resource. Read more about lists as nested resources [here](/cloud/trello/guides/rest-api/nested-resources/). (optional) (default to open)
members = 'none' # str | This is a nested resource. Read more about members as nested resources [here](/cloud/trello/guides/rest-api/nested-resources/). (optional) (default to none)
memberships = 'none' # str | This is a nested resource. Read more about memberships as nested resources [here](/cloud/trello/guides/rest-api/nested-resources/). (optional) (default to none)
plugin_data = false # bool | Determines whether the pluginData for this board should be returned. Valid values: true or false. (optional) (default to false)
organization = false # bool | This is a nested resource. Read more about organizations as nested resources [here](/cloud/trello/guides/rest-api/nested-resources/). (optional) (default to false)
organization_plugin_data = false # bool | Use with the `organization` param to include organization pluginData with the response (optional) (default to false)
my_prefs = false # bool |  (optional) (default to false)
tags = false # bool | Also known as collections, tags, refer to the collection(s) that a Board belongs to. (optional) (default to false)

try:
    # Get a Board
    api_response = api_instance.get_boards_id(id, actions=actions, board_stars=board_stars, cards=cards, card_plugin_data=card_plugin_data, checklists=checklists, custom_fields=custom_fields, fields=fields, labels=labels, lists=lists, members=members, memberships=memberships, plugin_data=plugin_data, organization=organization, organization_plugin_data=organization_plugin_data, my_prefs=my_prefs, tags=tags)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_boards_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)|  | 
 **actions** | **str**| This is a nested resource. Read more about actions as nested resources [here](/cloud/trello/guides/rest-api/nested-resources/). | [optional] [default to all]
 **board_stars** | **str**| Valid values are one of: &#x60;mine&#x60; or &#x60;none&#x60;. | [optional] [default to none]
 **cards** | **str**| This is a nested resource. Read more about cards as nested resources [here](/cloud/trello/guides/rest-api/nested-resources/). | [optional] [default to none]
 **card_plugin_data** | **bool**| Use with the &#x60;cards&#x60; param to include card pluginData with the response | [optional] [default to false]
 **checklists** | **str**| This is a nested resource. Read more about checklists as nested resources [here](/cloud/trello/guides/rest-api/nested-resources/). | [optional] [default to none]
 **custom_fields** | **bool**| This is a nested resource. Read more about custom fields as nested resources [here](#custom-fields-nested-resource). | [optional] [default to false]
 **fields** | **str**| The fields of the board to be included in the response. Valid values: all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idMemberCreator, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed, url | [optional] [default to name,desc,descData,closed,idOrganization,pinned,url,shortUrl,prefs,labelNames]
 **labels** | **str**| This is a nested resource. Read more about labels as nested resources [here](/cloud/trello/guides/rest-api/nested-resources/). | [optional] 
 **lists** | **str**| This is a nested resource. Read more about lists as nested resources [here](/cloud/trello/guides/rest-api/nested-resources/). | [optional] [default to open]
 **members** | **str**| This is a nested resource. Read more about members as nested resources [here](/cloud/trello/guides/rest-api/nested-resources/). | [optional] [default to none]
 **memberships** | **str**| This is a nested resource. Read more about memberships as nested resources [here](/cloud/trello/guides/rest-api/nested-resources/). | [optional] [default to none]
 **plugin_data** | **bool**| Determines whether the pluginData for this board should be returned. Valid values: true or false. | [optional] [default to false]
 **organization** | **bool**| This is a nested resource. Read more about organizations as nested resources [here](/cloud/trello/guides/rest-api/nested-resources/). | [optional] [default to false]
 **organization_plugin_data** | **bool**| Use with the &#x60;organization&#x60; param to include organization pluginData with the response | [optional] [default to false]
 **my_prefs** | **bool**|  | [optional] [default to false]
 **tags** | **bool**| Also known as collections, tags, refer to the collection(s) that a Board belongs to. | [optional] [default to false]

### Return type

[**Board**](Board.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_boards_id_actions**
> get_boards_id_actions(board_id, fields=fields, filter=filter, format=format, id_models=id_models, limit=limit, member=member, member_fields=member_fields, member_creator=member_creator, member_creator_fields=member_creator_fields, page=page, reactions=reactions, before=before, since=since)

Get Actions of a Board

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
board_id = 'board_id_example' # str | 
fields = trello_api_client.Action() # Action | The fields to be returned for the Actions. [See Action fields here](/cloud/trello/guides/rest-api/object-definitions/#action-object). (optional)
filter = 'filter_example' # str | A comma-separated list of [action types](/cloud/trello/guides/rest-api/action-types/). (optional)
format = 'list' # str | The format of the returned Actions. Either list or count. (optional) (default to list)
id_models = 'id_models_example' # str | A comma-separated list of idModels. Only actions related to these models will be returned. (optional)
limit = 50 # float | The limit of the number of responses, between 0 and 1000. (optional) (default to 50)
member = true # bool | Whether to return the member object for each action. (optional) (default to true)
member_fields = 'activityBlocked,avatarHash,avatarUrl,fullName,idMemberReferrer,initials,nonPublic,nonPublicAvailable,username' # str | The fields of the [member](/cloud/trello/guides/rest-api/object-definitions/#member-object) to return. (optional) (default to activityBlocked,avatarHash,avatarUrl,fullName,idMemberReferrer,initials,nonPublic,nonPublicAvailable,username)
member_creator = true # bool | Whether to return the memberCreator object for each action. (optional) (default to true)
member_creator_fields = 'activityBlocked,avatarHash,avatarUrl,fullName,idMemberReferrer,initials,nonPublic,nonPublicAvailable,username' # str | The fields of the [member](/cloud/trello/guides/rest-api/object-definitions/#member-object) creator to return (optional) (default to activityBlocked,avatarHash,avatarUrl,fullName,idMemberReferrer,initials,nonPublic,nonPublicAvailable,username)
page = 0 # float | The page of results for actions. (optional) (default to 0)
reactions = true # bool | Whether to show reactions on comments or not. (optional)
before = 'before_example' # str | An Action ID (optional)
since = 'since_example' # str | An Action ID (optional)

try:
    # Get Actions of a Board
    api_instance.get_boards_id_actions(board_id, fields=fields, filter=filter, format=format, id_models=id_models, limit=limit, member=member, member_fields=member_fields, member_creator=member_creator, member_creator_fields=member_creator_fields, page=page, reactions=reactions, before=before, since=since)
except ApiException as e:
    print("Exception when calling DefaultApi->get_boards_id_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_id** | **str**|  | 
 **fields** | [**Action**](.md)| The fields to be returned for the Actions. [See Action fields here](/cloud/trello/guides/rest-api/object-definitions/#action-object). | [optional] 
 **filter** | **str**| A comma-separated list of [action types](/cloud/trello/guides/rest-api/action-types/). | [optional] 
 **format** | **str**| The format of the returned Actions. Either list or count. | [optional] [default to list]
 **id_models** | **str**| A comma-separated list of idModels. Only actions related to these models will be returned. | [optional] 
 **limit** | **float**| The limit of the number of responses, between 0 and 1000. | [optional] [default to 50]
 **member** | **bool**| Whether to return the member object for each action. | [optional] [default to true]
 **member_fields** | **str**| The fields of the [member](/cloud/trello/guides/rest-api/object-definitions/#member-object) to return. | [optional] [default to activityBlocked,avatarHash,avatarUrl,fullName,idMemberReferrer,initials,nonPublic,nonPublicAvailable,username]
 **member_creator** | **bool**| Whether to return the memberCreator object for each action. | [optional] [default to true]
 **member_creator_fields** | **str**| The fields of the [member](/cloud/trello/guides/rest-api/object-definitions/#member-object) creator to return | [optional] [default to activityBlocked,avatarHash,avatarUrl,fullName,idMemberReferrer,initials,nonPublic,nonPublicAvailable,username]
 **page** | **float**| The page of results for actions. | [optional] [default to 0]
 **reactions** | **bool**| Whether to show reactions on comments or not. | [optional] 
 **before** | **str**| An Action ID | [optional] 
 **since** | **str**| An Action ID | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_boards_id_boardplugins**
> list[Plugin] get_boards_id_boardplugins(id)

Get Enabled Power-Ups on Board

Get the enabled Power-Ups on a board

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Board

try:
    # Get Enabled Power-Ups on Board
    api_response = api_instance.get_boards_id_boardplugins(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_boards_id_boardplugins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Board | 

### Return type

[**list[Plugin]**](Plugin.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_boards_id_boardstars**
> list[object] get_boards_id_boardstars(board_id, filter=filter)

Get boardStars on a Board

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
board_id = 'board_id_example' # str | 
filter = 'mine' # str | Valid values: mine, none (optional) (default to mine)

try:
    # Get boardStars on a Board
    api_response = api_instance.get_boards_id_boardstars(board_id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_boards_id_boardstars: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **board_id** | **str**|  | 
 **filter** | **str**| Valid values: mine, none | [optional] [default to mine]

### Return type

**list[object]**

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_boards_id_cards**
> get_boards_id_cards(id)

Get Cards on a Board

Get all of the open Cards on a Board.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get Cards on a Board
    api_instance.get_boards_id_cards(id)
except ApiException as e:
    print("Exception when calling DefaultApi->get_boards_id_cards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_boards_id_cards_filter**
> get_boards_id_cards_filter(id, filter)

Get filtered Cards on a Board

Get the Cards on a Board that match a given filter.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = 'id_example' # str | ID of the Board
filter = 'filter_example' # str | Valid Values: all, closed, none, open, visible.

try:
    # Get filtered Cards on a Board
    api_instance.get_boards_id_cards_filter(id, filter)
except ApiException as e:
    print("Exception when calling DefaultApi->get_boards_id_cards_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the Board | 
 **filter** | **str**| Valid Values: all, closed, none, open, visible. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_boards_id_cards_idcard**
> get_boards_id_cards_idcard(id, id_card, fields=fields, filter=filter, format=format, id_models=id_models, limit=limit, member=member, member_fields=member_fields, member_creator=member_creator, member_creator_fields=member_creator_fields, page=page, reactions=reactions, before=before, since=since)

Get a Card on a Board

Get a single Card on a Board.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the board
id_card = 'id_card_example' # str | The id the card to retrieve.
fields = trello_api_client.Action() # Action | The fields to be returned for the Actions. [See Action fields here](/cloud/trello/guides/rest-api/object-definitions/#action-object). (optional)
filter = 'filter_example' # str | A comma-separated list of [action types](/cloud/trello/guides/rest-api/action-types/). (optional)
format = 'list' # str | The format of the returned Actions. Either list or count. (optional) (default to list)
id_models = 'id_models_example' # str | A comma-separated list of idModels. Only actions related to these models will be returned. (optional)
limit = 50 # float | The limit of the number of responses, between 0 and 1000. (optional) (default to 50)
member = true # bool | Whether to return the member object for each action. (optional) (default to true)
member_fields = 'activityBlocked,avatarHash,avatarUrl,fullName,idMemberReferrer,initials,nonPublic,nonPublicAvailable,username' # str | The fields of the [member](/cloud/trello/guides/rest-api/object-definitions/#member-object) to return. (optional) (default to activityBlocked,avatarHash,avatarUrl,fullName,idMemberReferrer,initials,nonPublic,nonPublicAvailable,username)
member_creator = true # bool | Whether to return the memberCreator object for each action. (optional) (default to true)
member_creator_fields = 'activityBlocked,avatarHash,avatarUrl,fullName,idMemberReferrer,initials,nonPublic,nonPublicAvailable,username' # str | The fields of the [member](/cloud/trello/guides/rest-api/object-definitions/#member-object) creator to return (optional) (default to activityBlocked,avatarHash,avatarUrl,fullName,idMemberReferrer,initials,nonPublic,nonPublicAvailable,username)
page = 0 # float | The page of results for actions. (optional) (default to 0)
reactions = true # bool | Whether to show reactions on comments or not. (optional)
before = 'before_example' # str | An Action ID (optional)
since = 'since_example' # str | An Action ID (optional)

try:
    # Get a Card on a Board
    api_instance.get_boards_id_cards_idcard(id, id_card, fields=fields, filter=filter, format=format, id_models=id_models, limit=limit, member=member, member_fields=member_fields, member_creator=member_creator, member_creator_fields=member_creator_fields, page=page, reactions=reactions, before=before, since=since)
except ApiException as e:
    print("Exception when calling DefaultApi->get_boards_id_cards_idcard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the board | 
 **id_card** | **str**| The id the card to retrieve. | 
 **fields** | [**Action**](.md)| The fields to be returned for the Actions. [See Action fields here](/cloud/trello/guides/rest-api/object-definitions/#action-object). | [optional] 
 **filter** | **str**| A comma-separated list of [action types](/cloud/trello/guides/rest-api/action-types/). | [optional] 
 **format** | **str**| The format of the returned Actions. Either list or count. | [optional] [default to list]
 **id_models** | **str**| A comma-separated list of idModels. Only actions related to these models will be returned. | [optional] 
 **limit** | **float**| The limit of the number of responses, between 0 and 1000. | [optional] [default to 50]
 **member** | **bool**| Whether to return the member object for each action. | [optional] [default to true]
 **member_fields** | **str**| The fields of the [member](/cloud/trello/guides/rest-api/object-definitions/#member-object) to return. | [optional] [default to activityBlocked,avatarHash,avatarUrl,fullName,idMemberReferrer,initials,nonPublic,nonPublicAvailable,username]
 **member_creator** | **bool**| Whether to return the memberCreator object for each action. | [optional] [default to true]
 **member_creator_fields** | **str**| The fields of the [member](/cloud/trello/guides/rest-api/object-definitions/#member-object) creator to return | [optional] [default to activityBlocked,avatarHash,avatarUrl,fullName,idMemberReferrer,initials,nonPublic,nonPublicAvailable,username]
 **page** | **float**| The page of results for actions. | [optional] [default to 0]
 **reactions** | **bool**| Whether to show reactions on comments or not. | [optional] 
 **before** | **str**| An Action ID | [optional] 
 **since** | **str**| An Action ID | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_boards_id_customfields**
> list[CustomField] get_boards_id_customfields(id)

Get Custom Fields for Board

Get the Custom Field Definitions that exist on a board.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the board

try:
    # Get Custom Fields for Board
    api_response = api_instance.get_boards_id_customfields(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_boards_id_customfields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the board | 

### Return type

[**list[CustomField]**](CustomField.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_boards_id_field**
> get_boards_id_field(id, field)

Get a field on a Board

Get a single, specific field on a board

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the board.
field = 'field_example' # str | The field you'd like to receive. Valid values: closed, dateLastActivity, dateLastView, desc, descData, idMemberCreator, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed, url.

try:
    # Get a field on a Board
    api_instance.get_boards_id_field(id, field)
except ApiException as e:
    print("Exception when calling DefaultApi->get_boards_id_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the board. | 
 **field** | **str**| The field you&#x27;d like to receive. Valid values: closed, dateLastActivity, dateLastView, desc, descData, idMemberCreator, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed, url. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_boards_id_labels**
> get_boards_id_labels(id, fields=fields, limit=limit)

Get Labels on a Board

Get all of the Labels on a Board.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Board.
fields = trello_api_client.Label() # Label | The fields to be returned for the Labels. (optional)
limit = 50 # int | The number of Labels to be returned. (optional) (default to 50)

try:
    # Get Labels on a Board
    api_instance.get_boards_id_labels(id, fields=fields, limit=limit)
except ApiException as e:
    print("Exception when calling DefaultApi->get_boards_id_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Board. | 
 **fields** | [**Label**](.md)| The fields to be returned for the Labels. | [optional] 
 **limit** | **int**| The number of Labels to be returned. | [optional] [default to 50]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_boards_id_lists**
> list[TrelloList] get_boards_id_lists(id, cards=cards, card_fields=card_fields, filter=filter, fields=fields)

Get Lists on a Board

Get the Lists on a Board

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the board
cards = trello_api_client.ViewFilter() # ViewFilter | Filter to apply to Cards. (optional)
card_fields = 'all' # str | `all` or a comma-separated list of card [fields](/cloud/trello/guides/rest-api/object-definitions/#card-object) (optional) (default to all)
filter = trello_api_client.ViewFilter() # ViewFilter | Filter to apply to Lists (optional)
fields = 'all' # str | `all` or a comma-separated list of list [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional) (default to all)

try:
    # Get Lists on a Board
    api_response = api_instance.get_boards_id_lists(id, cards=cards, card_fields=card_fields, filter=filter, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_boards_id_lists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the board | 
 **cards** | [**ViewFilter**](.md)| Filter to apply to Cards. | [optional] 
 **card_fields** | **str**| &#x60;all&#x60; or a comma-separated list of card [fields](/cloud/trello/guides/rest-api/object-definitions/#card-object) | [optional] [default to all]
 **filter** | [**ViewFilter**](.md)| Filter to apply to Lists | [optional] 
 **fields** | **str**| &#x60;all&#x60; or a comma-separated list of list [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] [default to all]

### Return type

[**list[TrelloList]**](TrelloList.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_boards_id_lists_filter**
> get_boards_id_lists_filter(id, filter)

Get filtered Lists on a Board

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the board
filter = trello_api_client.ViewFilter() # ViewFilter | One of `all`, `closed`, `none`, `open`

try:
    # Get filtered Lists on a Board
    api_instance.get_boards_id_lists_filter(id, filter)
except ApiException as e:
    print("Exception when calling DefaultApi->get_boards_id_lists_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the board | 
 **filter** | [**ViewFilter**](.md)| One of &#x60;all&#x60;, &#x60;closed&#x60;, &#x60;none&#x60;, &#x60;open&#x60; | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_boards_id_members**
> get_boards_id_members(id)

Get the Members of a Board

Get the Members for a board

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the board

try:
    # Get the Members of a Board
    api_instance.get_boards_id_members(id)
except ApiException as e:
    print("Exception when calling DefaultApi->get_boards_id_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the board | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_boards_id_memberships**
> Memberships get_boards_id_memberships(id, filter=filter, activity=activity, org_member_type=org_member_type, member=member, member_fields=member_fields)

Get Memberships of a Board

Get information about the memberships users have to the board.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the board
filter = 'all' # str | One of `admins`, `all`, `none`, `normal` (optional) (default to all)
activity = false # bool | Works for premium organizations only. (optional) (default to false)
org_member_type = false # bool | Shows the type of member to the org the user is. For instance, an org admin will have a `orgMemberType` of `admin`. (optional) (default to false)
member = false # bool | Determines whether to include a [nested member object](/cloud/trello/guides/rest-api/nested-resources/). (optional) (default to false)
member_fields = trello_api_client.MemberFields() # MemberFields | Fields to show if `member=true`. Valid values: [nested member resource fields](/cloud/trello/guides/rest-api/nested-resources/). (optional)

try:
    # Get Memberships of a Board
    api_response = api_instance.get_boards_id_memberships(id, filter=filter, activity=activity, org_member_type=org_member_type, member=member, member_fields=member_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_boards_id_memberships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the board | 
 **filter** | **str**| One of &#x60;admins&#x60;, &#x60;all&#x60;, &#x60;none&#x60;, &#x60;normal&#x60; | [optional] [default to all]
 **activity** | **bool**| Works for premium organizations only. | [optional] [default to false]
 **org_member_type** | **bool**| Shows the type of member to the org the user is. For instance, an org admin will have a &#x60;orgMemberType&#x60; of &#x60;admin&#x60;. | [optional] [default to false]
 **member** | **bool**| Determines whether to include a [nested member object](/cloud/trello/guides/rest-api/nested-resources/). | [optional] [default to false]
 **member_fields** | [**MemberFields**](.md)| Fields to show if &#x60;member&#x3D;true&#x60;. Valid values: [nested member resource fields](/cloud/trello/guides/rest-api/nested-resources/). | [optional] 

### Return type

[**Memberships**](Memberships.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cards_id**
> Card get_cards_id(id, fields=fields, actions=actions, attachments=attachments, attachment_fields=attachment_fields, members=members, member_fields=member_fields, members_voted=members_voted, member_voted_fields=member_voted_fields, check_item_states=check_item_states, checklists=checklists, checklist_fields=checklist_fields, board=board, board_fields=board_fields, list=list, plugin_data=plugin_data, stickers=stickers, sticker_fields=sticker_fields, custom_field_items=custom_field_items)

Get a Card

Get a card by its ID

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
fields = 'fields_example' # str | `all` or a comma-separated list of [fields](/cloud/trello/guides/rest-api/object-definitions/). **Defaults**: `badges, checkItemStates, closed, dateLastActivity, desc, descData, due, start, email, idBoard, idChecklists, idLabels, idList, idMembers, idShort, idAttachmentCover, manualCoverAttachment, labels, name, pos, shortUrl, url` (optional)
actions = 'actions_example' # str | See the [Actions Nested Resource](/cloud/trello/guides/rest-api/nested-resources/#actions-nested-resource) (optional)
attachments = trello_api_client.Attachments() # Attachments | `true`, `false`, or `cover` (optional)
attachment_fields = 'all' # str | `all` or a comma-separated list of attachment [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional) (default to all)
members = false # bool | Whether to return member objects for members on the card (optional) (default to false)
member_fields = 'member_fields_example' # str | `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/). **Defaults**: `avatarHash, fullName, initials, username` (optional)
members_voted = false # bool | Whether to return member objects for members who voted on the card (optional) (default to false)
member_voted_fields = 'member_voted_fields_example' # str | `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/). **Defaults**: `avatarHash, fullName, initials, username` (optional)
check_item_states = false # bool |  (optional) (default to false)
checklists = 'none' # str | Whether to return the checklists on the card. `all` or `none` (optional) (default to none)
checklist_fields = 'all' # str | `all` or a comma-separated list of `idBoard,idCard,name,pos` (optional) (default to all)
board = false # bool | Whether to return the board object the card is on (optional) (default to false)
board_fields = 'board_fields_example' # str | `all` or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/#board-object). **Defaults**: `name, desc, descData, closed, idOrganization, pinned, url, prefs` (optional)
list = false # bool | See the [Lists Nested Resource](/cloud/trello/guides/rest-api/nested-resources/) (optional) (default to false)
plugin_data = false # bool | Whether to include pluginData on the card with the response (optional) (default to false)
stickers = false # bool | Whether to include sticker models with the response (optional) (default to false)
sticker_fields = 'all' # str | `all` or a comma-separated list of sticker [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional) (default to all)
custom_field_items = false # bool | Whether to include the customFieldItems (optional) (default to false)

try:
    # Get a Card
    api_response = api_instance.get_cards_id(id, fields=fields, actions=actions, attachments=attachments, attachment_fields=attachment_fields, members=members, member_fields=member_fields, members_voted=members_voted, member_voted_fields=member_voted_fields, check_item_states=check_item_states, checklists=checklists, checklist_fields=checklist_fields, board=board, board_fields=board_fields, list=list, plugin_data=plugin_data, stickers=stickers, sticker_fields=sticker_fields, custom_field_items=custom_field_items)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cards_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **fields** | **str**| &#x60;all&#x60; or a comma-separated list of [fields](/cloud/trello/guides/rest-api/object-definitions/). **Defaults**: &#x60;badges, checkItemStates, closed, dateLastActivity, desc, descData, due, start, email, idBoard, idChecklists, idLabels, idList, idMembers, idShort, idAttachmentCover, manualCoverAttachment, labels, name, pos, shortUrl, url&#x60; | [optional] 
 **actions** | **str**| See the [Actions Nested Resource](/cloud/trello/guides/rest-api/nested-resources/#actions-nested-resource) | [optional] 
 **attachments** | [**Attachments**](.md)| &#x60;true&#x60;, &#x60;false&#x60;, or &#x60;cover&#x60; | [optional] 
 **attachment_fields** | **str**| &#x60;all&#x60; or a comma-separated list of attachment [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] [default to all]
 **members** | **bool**| Whether to return member objects for members on the card | [optional] [default to false]
 **member_fields** | **str**| &#x60;all&#x60; or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/). **Defaults**: &#x60;avatarHash, fullName, initials, username&#x60; | [optional] 
 **members_voted** | **bool**| Whether to return member objects for members who voted on the card | [optional] [default to false]
 **member_voted_fields** | **str**| &#x60;all&#x60; or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/). **Defaults**: &#x60;avatarHash, fullName, initials, username&#x60; | [optional] 
 **check_item_states** | **bool**|  | [optional] [default to false]
 **checklists** | **str**| Whether to return the checklists on the card. &#x60;all&#x60; or &#x60;none&#x60; | [optional] [default to none]
 **checklist_fields** | **str**| &#x60;all&#x60; or a comma-separated list of &#x60;idBoard,idCard,name,pos&#x60; | [optional] [default to all]
 **board** | **bool**| Whether to return the board object the card is on | [optional] [default to false]
 **board_fields** | **str**| &#x60;all&#x60; or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/#board-object). **Defaults**: &#x60;name, desc, descData, closed, idOrganization, pinned, url, prefs&#x60; | [optional] 
 **list** | **bool**| See the [Lists Nested Resource](/cloud/trello/guides/rest-api/nested-resources/) | [optional] [default to false]
 **plugin_data** | **bool**| Whether to include pluginData on the card with the response | [optional] [default to false]
 **stickers** | **bool**| Whether to include sticker models with the response | [optional] [default to false]
 **sticker_fields** | **str**| &#x60;all&#x60; or a comma-separated list of sticker [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] [default to all]
 **custom_field_items** | **bool**| Whether to include the customFieldItems | [optional] [default to false]

### Return type

[**Card**](Card.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cards_id_actions**
> list[Action] get_cards_id_actions(id, filter=filter, page=page)

Get Actions on a Card

List the Actions on a Card

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
filter = 'commentCard, updateCard:idList' # str | A comma-separated list of [action types](https://developer.atlassian.com/cloud/trello/guides/rest-api/action-types/). (optional) (default to commentCard, updateCard:idList)
page = 0 # float | The page of results for actions. Each page of results has 50 actions. (optional) (default to 0)

try:
    # Get Actions on a Card
    api_response = api_instance.get_cards_id_actions(id, filter=filter, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cards_id_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **filter** | **str**| A comma-separated list of [action types](https://developer.atlassian.com/cloud/trello/guides/rest-api/action-types/). | [optional] [default to commentCard, updateCard:idList]
 **page** | **float**| The page of results for actions. Each page of results has 50 actions. | [optional] [default to 0]

### Return type

[**list[Action]**](Action.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cards_id_attachments**
> list[object] get_cards_id_attachments(id, fields=fields, filter=filter)

Get Attachments on a Card

List the attachments on a card

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
fields = 'all' # str | `all` or a comma-separated list of attachment [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional) (default to all)
filter = 'false' # str | Use `cover` to restrict to just the cover attachment (optional) (default to false)

try:
    # Get Attachments on a Card
    api_response = api_instance.get_cards_id_attachments(id, fields=fields, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cards_id_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **fields** | **str**| &#x60;all&#x60; or a comma-separated list of attachment [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] [default to all]
 **filter** | **str**| Use &#x60;cover&#x60; to restrict to just the cover attachment | [optional] [default to false]

### Return type

**list[object]**

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cards_id_attachments_idattachment**
> list[object] get_cards_id_attachments_idattachment(id, id_attachment, fields=fields)

Get an Attachment on a Card

Get a specific Attachment on a Card.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
id_attachment = trello_api_client.TrelloID() # TrelloID | The ID of the Attachment
fields = [["all"]] # list[object] | The Attachment fields to be included in the response. (optional) (default to ["all"])

try:
    # Get an Attachment on a Card
    api_response = api_instance.get_cards_id_attachments_idattachment(id, id_attachment, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cards_id_attachments_idattachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **id_attachment** | [**TrelloID**](.md)| The ID of the Attachment | 
 **fields** | [**list[object]**](object.md)| The Attachment fields to be included in the response. | [optional] [default to [&quot;all&quot;]]

### Return type

**list[object]**

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cards_id_board**
> get_cards_id_board(id, fields=fields)

Get the Board the Card is on

Get the board a card is on

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
fields = 'all' # str | `all` or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/#board-object) (optional) (default to all)

try:
    # Get the Board the Card is on
    api_instance.get_cards_id_board(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cards_id_board: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **fields** | **str**| &#x60;all&#x60; or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/#board-object) | [optional] [default to all]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cards_id_checkitem_idcheckitem**
> get_cards_id_checkitem_idcheckitem(id, id_check_item, fields=fields)

Get checkItem on a Card

Get a specific checkItem on a card

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
id_check_item = trello_api_client.TrelloID() # TrelloID | The ID of the checkitem
fields = 'name,nameData,pos,state,due,dueReminder,idMember' # str | `all` or a comma-separated list of `name,nameData,pos,state,type,due,dueReminder,idMember` (optional) (default to name,nameData,pos,state,due,dueReminder,idMember)

try:
    # Get checkItem on a Card
    api_instance.get_cards_id_checkitem_idcheckitem(id, id_check_item, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cards_id_checkitem_idcheckitem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **id_check_item** | [**TrelloID**](.md)| The ID of the checkitem | 
 **fields** | **str**| &#x60;all&#x60; or a comma-separated list of &#x60;name,nameData,pos,state,type,due,dueReminder,idMember&#x60; | [optional] [default to name,nameData,pos,state,due,dueReminder,idMember]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cards_id_checkitemstates**
> get_cards_id_checkitemstates(id, fields=fields)

Get checkItems on a Card

Get the completed checklist items on a card

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
fields = 'all' # str | `all` or a comma-separated list of: `idCheckItem`, `state` (optional) (default to all)

try:
    # Get checkItems on a Card
    api_instance.get_cards_id_checkitemstates(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cards_id_checkitemstates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **fields** | **str**| &#x60;all&#x60; or a comma-separated list of: &#x60;idCheckItem&#x60;, &#x60;state&#x60; | [optional] [default to all]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cards_id_checklists**
> get_cards_id_checklists(id, check_items=check_items, check_item_fields=check_item_fields, filter=filter, fields=fields)

Get Checklists on a Card

Get the checklists on a card

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
check_items = 'all' # str | `all` or `none` (optional) (default to all)
check_item_fields = 'name,nameData,pos,state,due,dueReminder,idMember' # str | `all` or a comma-separated list of: `name,nameData,pos,state,type,due,dueReminder,idMember` (optional) (default to name,nameData,pos,state,due,dueReminder,idMember)
filter = 'all' # str | `all` or `none` (optional) (default to all)
fields = 'all' # str | `all` or a comma-separated list of: `idBoard,idCard,name,pos` (optional) (default to all)

try:
    # Get Checklists on a Card
    api_instance.get_cards_id_checklists(id, check_items=check_items, check_item_fields=check_item_fields, filter=filter, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cards_id_checklists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **check_items** | **str**| &#x60;all&#x60; or &#x60;none&#x60; | [optional] [default to all]
 **check_item_fields** | **str**| &#x60;all&#x60; or a comma-separated list of: &#x60;name,nameData,pos,state,type,due,dueReminder,idMember&#x60; | [optional] [default to name,nameData,pos,state,due,dueReminder,idMember]
 **filter** | **str**| &#x60;all&#x60; or &#x60;none&#x60; | [optional] [default to all]
 **fields** | **str**| &#x60;all&#x60; or a comma-separated list of: &#x60;idBoard,idCard,name,pos&#x60; | [optional] [default to all]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cards_id_customfielditems**
> list[CustomFieldItems] get_cards_id_customfielditems(id)

Get Custom Field Items for a Card

Get the custom field items for a card.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card

try:
    # Get Custom Field Items for a Card
    api_response = api_instance.get_cards_id_customfielditems(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cards_id_customfielditems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 

### Return type

[**list[CustomFieldItems]**](CustomFieldItems.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cards_id_field**
> Card get_cards_id_field(id, field)

Get a field on a Card

Get a specific property of a card

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
field = trello_api_client.CardFields() # CardFields | The desired field.

try:
    # Get a field on a Card
    api_response = api_instance.get_cards_id_field(id, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cards_id_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **field** | [**CardFields**](.md)| The desired field. | 

### Return type

[**Card**](Card.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cards_id_list**
> get_cards_id_list(id, fields=fields)

Get the List of a Card

Get the list a card is in

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
fields = 'all' # str | `all` or a comma-separated list of list [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional) (default to all)

try:
    # Get the List of a Card
    api_instance.get_cards_id_list(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cards_id_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **fields** | **str**| &#x60;all&#x60; or a comma-separated list of list [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] [default to all]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cards_id_members**
> get_cards_id_members(id, fields=fields)

Get the Members of a Card

Get the members on a card

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
fields = 'avatarHash,fullName,initials,username' # str | `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional) (default to avatarHash,fullName,initials,username)

try:
    # Get the Members of a Card
    api_instance.get_cards_id_members(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cards_id_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **fields** | **str**| &#x60;all&#x60; or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] [default to avatarHash,fullName,initials,username]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cards_id_membersvoted**
> get_cards_id_membersvoted(id, fields=fields)

Get Members who have voted on a Card

Get the members who have voted on a card

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
fields = 'avatarHash,fullName,initials,username' # str | `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional) (default to avatarHash,fullName,initials,username)

try:
    # Get Members who have voted on a Card
    api_instance.get_cards_id_membersvoted(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cards_id_membersvoted: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **fields** | **str**| &#x60;all&#x60; or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] [default to avatarHash,fullName,initials,username]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cards_id_plugindata**
> get_cards_id_plugindata(id)

Get pluginData on a Card

Get any shared pluginData on a card.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card

try:
    # Get pluginData on a Card
    api_instance.get_cards_id_plugindata(id)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cards_id_plugindata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cards_id_stickers**
> get_cards_id_stickers(id, fields=fields)

Get Stickers on a Card

Get the stickers on a card

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
fields = 'all' # str | `all` or a comma-separated list of sticker [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional) (default to all)

try:
    # Get Stickers on a Card
    api_instance.get_cards_id_stickers(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cards_id_stickers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **fields** | **str**| &#x60;all&#x60; or a comma-separated list of sticker [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] [default to all]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cards_id_stickers_idsticker**
> get_cards_id_stickers_idsticker(id, id_sticker, fields=fields)

Get a Sticker on a Card

Get a specific sticker on a card

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
id_sticker = trello_api_client.TrelloID() # TrelloID | The ID of the sticker
fields = 'all' # str | `all` or a comma-separated list of sticker [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional) (default to all)

try:
    # Get a Sticker on a Card
    api_instance.get_cards_id_stickers_idsticker(id, id_sticker, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->get_cards_id_stickers_idsticker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **id_sticker** | [**TrelloID**](.md)| The ID of the sticker | 
 **fields** | **str**| &#x60;all&#x60; or a comma-separated list of sticker [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] [default to all]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checklists_id**
> get_checklists_id(id, cards=cards, check_items=check_items, check_item_fields=check_item_fields, fields=fields)

Get a Checklist

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of a checklist.
cards = 'none' # str | Valid values: `all`, `closed`, `none`, `open`, `visible`. Cards is a nested resource. The additional query params available are documented at [Cards Nested Resource](/cloud/trello/guides/rest-api/nested-resources/#cards-nested-resource). (optional) (default to none)
check_items = 'all' # str | The check items on the list to return. One of: `all`, `none`. (optional) (default to all)
check_item_fields = 'name, nameData, pos, state, due, dueReminder, idMember' # str | The fields on the checkItem to return if checkItems are being returned. `all` or a comma-separated list of: `name`, `nameData`, `pos`, `state`, `type`, `due`, `dueReminder`, `idMember` (optional) (default to name, nameData, pos, state, due, dueReminder, idMember)
fields = 'all' # str | `all` or a comma-separated list of checklist [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional) (default to all)

try:
    # Get a Checklist
    api_instance.get_checklists_id(id, cards=cards, check_items=check_items, check_item_fields=check_item_fields, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->get_checklists_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of a checklist. | 
 **cards** | **str**| Valid values: &#x60;all&#x60;, &#x60;closed&#x60;, &#x60;none&#x60;, &#x60;open&#x60;, &#x60;visible&#x60;. Cards is a nested resource. The additional query params available are documented at [Cards Nested Resource](/cloud/trello/guides/rest-api/nested-resources/#cards-nested-resource). | [optional] [default to none]
 **check_items** | **str**| The check items on the list to return. One of: &#x60;all&#x60;, &#x60;none&#x60;. | [optional] [default to all]
 **check_item_fields** | **str**| The fields on the checkItem to return if checkItems are being returned. &#x60;all&#x60; or a comma-separated list of: &#x60;name&#x60;, &#x60;nameData&#x60;, &#x60;pos&#x60;, &#x60;state&#x60;, &#x60;type&#x60;, &#x60;due&#x60;, &#x60;dueReminder&#x60;, &#x60;idMember&#x60; | [optional] [default to name, nameData, pos, state, due, dueReminder, idMember]
 **fields** | **str**| &#x60;all&#x60; or a comma-separated list of checklist [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] [default to all]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checklists_id_board**
> get_checklists_id_board(id, fields=fields)

Get the Board the Checklist is on

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of a checklist.
fields = 'all' # str | `all` or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional) (default to all)

try:
    # Get the Board the Checklist is on
    api_instance.get_checklists_id_board(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->get_checklists_id_board: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of a checklist. | 
 **fields** | **str**| &#x60;all&#x60; or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] [default to all]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checklists_id_cards**
> get_checklists_id_cards(id)

Get the Card a Checklist is on

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of a checklist.

try:
    # Get the Card a Checklist is on
    api_instance.get_checklists_id_cards(id)
except ApiException as e:
    print("Exception when calling DefaultApi->get_checklists_id_cards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of a checklist. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checklists_id_checkitems**
> get_checklists_id_checkitems(id, filter=filter, fields=fields)

Get Checkitems on a Checklist

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of a checklist.
filter = 'all' # str | One of: `all`, `none`. (optional) (default to all)
fields = 'name, nameData, pos, state, due, dueReminder, idMember' # str | One of: `all`, `name`, `nameData`, `pos`, `state`,`type`, `due`, `dueReminder`, `idMember`. (optional) (default to name, nameData, pos, state, due, dueReminder, idMember)

try:
    # Get Checkitems on a Checklist
    api_instance.get_checklists_id_checkitems(id, filter=filter, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->get_checklists_id_checkitems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of a checklist. | 
 **filter** | **str**| One of: &#x60;all&#x60;, &#x60;none&#x60;. | [optional] [default to all]
 **fields** | **str**| One of: &#x60;all&#x60;, &#x60;name&#x60;, &#x60;nameData&#x60;, &#x60;pos&#x60;, &#x60;state&#x60;,&#x60;type&#x60;, &#x60;due&#x60;, &#x60;dueReminder&#x60;, &#x60;idMember&#x60;. | [optional] [default to name, nameData, pos, state, due, dueReminder, idMember]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checklists_id_checkitems_idcheckitem**
> get_checklists_id_checkitems_idcheckitem(id, id_check_item, fields=fields)

Get a Checkitem on a Checklist

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of a checklist.
id_check_item = trello_api_client.TrelloID() # TrelloID | ID of the check item to retrieve.
fields = 'name, nameData, pos, state, due, dueReminder, idMember' # str | One of: `all`, `name`, `nameData`, `pos`, `state`, `type`, `due`, `dueReminder`, `idMember`,. (optional) (default to name, nameData, pos, state, due, dueReminder, idMember)

try:
    # Get a Checkitem on a Checklist
    api_instance.get_checklists_id_checkitems_idcheckitem(id, id_check_item, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->get_checklists_id_checkitems_idcheckitem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of a checklist. | 
 **id_check_item** | [**TrelloID**](.md)| ID of the check item to retrieve. | 
 **fields** | **str**| One of: &#x60;all&#x60;, &#x60;name&#x60;, &#x60;nameData&#x60;, &#x60;pos&#x60;, &#x60;state&#x60;, &#x60;type&#x60;, &#x60;due&#x60;, &#x60;dueReminder&#x60;, &#x60;idMember&#x60;,. | [optional] [default to name, nameData, pos, state, due, dueReminder, idMember]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checklists_id_field**
> get_checklists_id_field(id, field)

Get field on a Checklist

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of a checklist.
field = 'field_example' # str | Field to update.

try:
    # Get field on a Checklist
    api_instance.get_checklists_id_field(id, field)
except ApiException as e:
    print("Exception when calling DefaultApi->get_checklists_id_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of a checklist. | 
 **field** | **str**| Field to update. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customfields_id**
> CustomField get_customfields_id(id)

Get a Custom Field

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the Custom Field.

try:
    # Get a Custom Field
    api_response = api_instance.get_customfields_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_customfields_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the Custom Field. | 

### Return type

[**CustomField**](CustomField.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customfields_id_options**
> get_customfields_id_options(id)

Add Option to Custom Field dropdown

Add an option to a dropdown Custom Field

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the customfield.

try:
    # Add Option to Custom Field dropdown
    api_instance.get_customfields_id_options(id)
except ApiException as e:
    print("Exception when calling DefaultApi->get_customfields_id_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the customfield. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customfields_options_idcustomfieldoption**
> get_customfields_options_idcustomfieldoption(id, id_custom_field_option)

Get Option of Custom Field dropdown

Retrieve a specific, existing Option on a given dropdown-type Custom Field

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the customfielditem.
id_custom_field_option = trello_api_client.TrelloID() # TrelloID | ID of the customfieldoption to retrieve.

try:
    # Get Option of Custom Field dropdown
    api_instance.get_customfields_options_idcustomfieldoption(id, id_custom_field_option)
except ApiException as e:
    print("Exception when calling DefaultApi->get_customfields_options_idcustomfieldoption: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the customfielditem. | 
 **id_custom_field_option** | [**TrelloID**](.md)| ID of the customfieldoption to retrieve. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enterprises_id**
> Enterprise get_enterprises_id(id, fields=fields, members=members, member_fields=member_fields, member_filter=member_filter, member_sort=member_sort, member_sort_by=member_sort_by, member_sort_order=member_sort_order, member_start_index=member_start_index, member_count=member_count, organizations=organizations, organization_fields=organization_fields, organization_paid_accounts=organization_paid_accounts, organization_memberships=organization_memberships)

Get an Enterprise

Get an enterprise by its ID.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the enterprise to retrieve.
fields = 'all' # str | Comma-separated list of: `id`, `name`, `displayName`, `prefs`, `ssoActivationFailed`, `idAdmins`, `idMembers` (Note that the members array returned will be paginated if `members` is 'normal' or 'admins'. Pagination can be controlled with member_startIndex, etc, but the API response will not contain the total available result count or pagination status data. Read the SCIM documentation [here]() for more information on filtering), `idOrganizations`, `products`, `userTypes`, `idMembers`, `idOrganizations` (optional) (default to all)
members = 'none' # str | One of: `none`, `normal`, `admins`, `owners`, `all` (optional) (default to none)
member_fields = 'avatarHash, fullName, initials, username' # str | One of: `avatarHash`, `fullName`, `initials`, `username` (optional) (default to avatarHash, fullName, initials, username)
member_filter = 'none' # str | Pass a [SCIM-style query](/cloud/trello/scim/) to filter members. This takes precedence over the all/normal/admins value of members. If any of the member_* args are set, the member array will be paginated. (optional) (default to none)
member_sort = 'member_sort_example' # str | This parameter expects a [SCIM-style](/cloud/trello/scim/) sorting value prefixed by a `-` to sort descending. If no `-` is prefixed, it will be sorted ascending. Note that the members array returned will be paginated if `members` is 'normal' or 'admins'. Pagination can be controlled with member_startIndex, etc, but the API response will not contain the total available result count or pagination status data. (optional)
member_sort_by = 'none' # str | Deprecated: Please use member_sort. This parameter expects a [SCIM-style sorting value](/cloud/trello/scim/). Note that the members array returned will be paginated if `members` is `normal` or `admins`. Pagination can be controlled with `member_startIndex`, etc, and the API response's header will contain the total count and pagination state. (optional) (default to none)
member_sort_order = 'id' # str | Deprecated: Please use member_sort. One of: `ascending`, `descending`, `asc`, `desc` (optional) (default to id)
member_start_index = 56 # int | Any integer between 0 and 100. (optional)
member_count = 56 # int | 0 to 100 (optional)
organizations = 'none' # str | One of: `none`, `members`, `public`, `all` (optional) (default to none)
organization_fields = 'none' # str | Any valid value that the [nested organization field resource]() accepts. (optional) (default to none)
organization_paid_accounts = false # bool | Whether or not to include paid account information in the returned workspace objects (optional) (default to false)
organization_memberships = 'none' # str | Comma-seperated list of: `me`, `normal`, `admin`, `active`, `deactivated` (optional) (default to none)

try:
    # Get an Enterprise
    api_response = api_instance.get_enterprises_id(id, fields=fields, members=members, member_fields=member_fields, member_filter=member_filter, member_sort=member_sort, member_sort_by=member_sort_by, member_sort_order=member_sort_order, member_start_index=member_start_index, member_count=member_count, organizations=organizations, organization_fields=organization_fields, organization_paid_accounts=organization_paid_accounts, organization_memberships=organization_memberships)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_enterprises_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the enterprise to retrieve. | 
 **fields** | **str**| Comma-separated list of: &#x60;id&#x60;, &#x60;name&#x60;, &#x60;displayName&#x60;, &#x60;prefs&#x60;, &#x60;ssoActivationFailed&#x60;, &#x60;idAdmins&#x60;, &#x60;idMembers&#x60; (Note that the members array returned will be paginated if &#x60;members&#x60; is &#x27;normal&#x27; or &#x27;admins&#x27;. Pagination can be controlled with member_startIndex, etc, but the API response will not contain the total available result count or pagination status data. Read the SCIM documentation [here]() for more information on filtering), &#x60;idOrganizations&#x60;, &#x60;products&#x60;, &#x60;userTypes&#x60;, &#x60;idMembers&#x60;, &#x60;idOrganizations&#x60; | [optional] [default to all]
 **members** | **str**| One of: &#x60;none&#x60;, &#x60;normal&#x60;, &#x60;admins&#x60;, &#x60;owners&#x60;, &#x60;all&#x60; | [optional] [default to none]
 **member_fields** | **str**| One of: &#x60;avatarHash&#x60;, &#x60;fullName&#x60;, &#x60;initials&#x60;, &#x60;username&#x60; | [optional] [default to avatarHash, fullName, initials, username]
 **member_filter** | **str**| Pass a [SCIM-style query](/cloud/trello/scim/) to filter members. This takes precedence over the all/normal/admins value of members. If any of the member_* args are set, the member array will be paginated. | [optional] [default to none]
 **member_sort** | **str**| This parameter expects a [SCIM-style](/cloud/trello/scim/) sorting value prefixed by a &#x60;-&#x60; to sort descending. If no &#x60;-&#x60; is prefixed, it will be sorted ascending. Note that the members array returned will be paginated if &#x60;members&#x60; is &#x27;normal&#x27; or &#x27;admins&#x27;. Pagination can be controlled with member_startIndex, etc, but the API response will not contain the total available result count or pagination status data. | [optional] 
 **member_sort_by** | **str**| Deprecated: Please use member_sort. This parameter expects a [SCIM-style sorting value](/cloud/trello/scim/). Note that the members array returned will be paginated if &#x60;members&#x60; is &#x60;normal&#x60; or &#x60;admins&#x60;. Pagination can be controlled with &#x60;member_startIndex&#x60;, etc, and the API response&#x27;s header will contain the total count and pagination state. | [optional] [default to none]
 **member_sort_order** | **str**| Deprecated: Please use member_sort. One of: &#x60;ascending&#x60;, &#x60;descending&#x60;, &#x60;asc&#x60;, &#x60;desc&#x60; | [optional] [default to id]
 **member_start_index** | **int**| Any integer between 0 and 100. | [optional] 
 **member_count** | **int**| 0 to 100 | [optional] 
 **organizations** | **str**| One of: &#x60;none&#x60;, &#x60;members&#x60;, &#x60;public&#x60;, &#x60;all&#x60; | [optional] [default to none]
 **organization_fields** | **str**| Any valid value that the [nested organization field resource]() accepts. | [optional] [default to none]
 **organization_paid_accounts** | **bool**| Whether or not to include paid account information in the returned workspace objects | [optional] [default to false]
 **organization_memberships** | **str**| Comma-seperated list of: &#x60;me&#x60;, &#x60;normal&#x60;, &#x60;admin&#x60;, &#x60;active&#x60;, &#x60;deactivated&#x60; | [optional] [default to none]

### Return type

[**Enterprise**](Enterprise.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enterprises_id_admins**
> EnterpriseAdmin get_enterprises_id_admins(id, fields=fields)

Get Enterprise admin Members

Get an enterprise's admin members.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the enterprise to retrieve.
fields = 'fullName, userName' # str | Any valid value that the [nested member field resource]() accepts. (optional) (default to fullName, userName)

try:
    # Get Enterprise admin Members
    api_response = api_instance.get_enterprises_id_admins(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_enterprises_id_admins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the enterprise to retrieve. | 
 **fields** | **str**| Any valid value that the [nested member field resource]() accepts. | [optional] [default to fullName, userName]

### Return type

[**EnterpriseAdmin**](EnterpriseAdmin.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enterprises_id_auditlog**
> list[EnterpriseAuditLog] get_enterprises_id_auditlog(id)

Get auditlog data for an Enterprise

Returns an array of Actions related to the Enterprise object. Used for populating data sent to Google Sheets from an Enterprise's audit log page: https://trello.com/e/{enterprise_name}/admin/auditlog. An Enterprise admin token is required for this route.    NOTE: For enterprises that have opted in to user management via AdminHub, the auditlog will will contain actions taken in AdminHub, but may not contain the source for those actions.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the enterprise to retrieve.

try:
    # Get auditlog data for an Enterprise
    api_response = api_instance.get_enterprises_id_auditlog(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_enterprises_id_auditlog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the enterprise to retrieve. | 

### Return type

[**list[EnterpriseAuditLog]**](EnterpriseAuditLog.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enterprises_id_claimable_organizations**
> ClaimableOrganizations get_enterprises_id_claimable_organizations(id, limit=limit, cursor=cursor, name=name, active_since=active_since, inactive_since=inactive_since)

Get ClaimableOrganizations of an Enterprise

Get the Workspaces that are claimable by the enterprise by ID. Can optionally query for workspaces based on activeness/ inactiveness.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the enterprise to retrieve
limit = 56 # int | Limits the number of workspaces to be sorted (optional)
cursor = 'cursor_example' # str | Specifies the sort order to return matching documents (optional)
name = 'name_example' # str | Name of the enterprise to retrieve workspaces for (optional)
active_since = 'active_since_example' # str | Date in YYYY-MM-DD format indicating the date to search up to for activeness of workspace (optional)
inactive_since = 'inactive_since_example' # str | Date in YYYY-MM-DD format indicating the date to search up to for inactiveness of workspace (optional)

try:
    # Get ClaimableOrganizations of an Enterprise
    api_response = api_instance.get_enterprises_id_claimable_organizations(id, limit=limit, cursor=cursor, name=name, active_since=active_since, inactive_since=inactive_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_enterprises_id_claimable_organizations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the enterprise to retrieve | 
 **limit** | **int**| Limits the number of workspaces to be sorted | [optional] 
 **cursor** | **str**| Specifies the sort order to return matching documents | [optional] 
 **name** | **str**| Name of the enterprise to retrieve workspaces for | [optional] 
 **active_since** | **str**| Date in YYYY-MM-DD format indicating the date to search up to for activeness of workspace | [optional] 
 **inactive_since** | **str**| Date in YYYY-MM-DD format indicating the date to search up to for inactiveness of workspace | [optional] 

### Return type

[**ClaimableOrganizations**](ClaimableOrganizations.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enterprises_id_members**
> list[Member] get_enterprises_id_members(id, fields=fields, filter=filter, sort=sort, sort_by=sort_by, sort_order=sort_order, start_index=start_index, count=count, organization_fields=organization_fields, board_fields=board_fields)

Get Members of Enterprise

Get the members of an enterprise.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the Enterprise to retrieve.
fields = 'avatarHash, fullName, initials, username' # str | A comma-seperated list of valid [member fields](/cloud/trello/guides/rest-api/object-definitions/#member-object). (optional) (default to avatarHash, fullName, initials, username)
filter = 'filter_example' # str | Pass a [SCIM-style query](/cloud/trello/scim/) to filter members. This takes precedence over the all/normal/admins value of members. If any of the below member_* args are set, the member array will be paginated. (optional)
sort = 'sort_example' # str | This parameter expects a [SCIM-style](/cloud/trello/scim/) sorting value prefixed by a `-` to sort descending. If no `-` is prefixed, it will be sorted ascending. Note that the members array returned will be paginated if `members` is 'normal' or 'admins'. Pagination can be controlled with member_startIndex, etc, but the API response will not contain the total available result count or pagination status data. (optional)
sort_by = 'sort_by_example' # str | Deprecated: Please use `sort` instead. This parameter expects a [SCIM-style](/cloud/trello/scim/) sorting value. Note that the members array returned will be paginated if `members` is 'normal' or 'admins'. Pagination can be controlled with member_startIndex, etc, but the API response will not contain the total available result count or pagination status data. (optional)
sort_order = 'sort_order_example' # str | Deprecated: Please use `sort` instead. One of: `ascending`, `descending`, `asc`, `desc`. (optional)
start_index = 56 # int | Any integer between 0 and 9999. (optional)
count = 'none' # str | [SCIM-style filter](/cloud/trello/scim/). (optional) (default to none)
organization_fields = 'displayName' # str | Any valid value that the [nested organization field resource](/cloud/trello/guides/rest-api/nested-resources/) accepts. (optional) (default to displayName)
board_fields = 'name' # str | Any valid value that the [nested board resource](/cloud/trello/guides/rest-api/nested-resources/) accepts. (optional) (default to name)

try:
    # Get Members of Enterprise
    api_response = api_instance.get_enterprises_id_members(id, fields=fields, filter=filter, sort=sort, sort_by=sort_by, sort_order=sort_order, start_index=start_index, count=count, organization_fields=organization_fields, board_fields=board_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_enterprises_id_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the Enterprise to retrieve. | 
 **fields** | **str**| A comma-seperated list of valid [member fields](/cloud/trello/guides/rest-api/object-definitions/#member-object). | [optional] [default to avatarHash, fullName, initials, username]
 **filter** | **str**| Pass a [SCIM-style query](/cloud/trello/scim/) to filter members. This takes precedence over the all/normal/admins value of members. If any of the below member_* args are set, the member array will be paginated. | [optional] 
 **sort** | **str**| This parameter expects a [SCIM-style](/cloud/trello/scim/) sorting value prefixed by a &#x60;-&#x60; to sort descending. If no &#x60;-&#x60; is prefixed, it will be sorted ascending. Note that the members array returned will be paginated if &#x60;members&#x60; is &#x27;normal&#x27; or &#x27;admins&#x27;. Pagination can be controlled with member_startIndex, etc, but the API response will not contain the total available result count or pagination status data. | [optional] 
 **sort_by** | **str**| Deprecated: Please use &#x60;sort&#x60; instead. This parameter expects a [SCIM-style](/cloud/trello/scim/) sorting value. Note that the members array returned will be paginated if &#x60;members&#x60; is &#x27;normal&#x27; or &#x27;admins&#x27;. Pagination can be controlled with member_startIndex, etc, but the API response will not contain the total available result count or pagination status data. | [optional] 
 **sort_order** | **str**| Deprecated: Please use &#x60;sort&#x60; instead. One of: &#x60;ascending&#x60;, &#x60;descending&#x60;, &#x60;asc&#x60;, &#x60;desc&#x60;. | [optional] 
 **start_index** | **int**| Any integer between 0 and 9999. | [optional] 
 **count** | **str**| [SCIM-style filter](/cloud/trello/scim/). | [optional] [default to none]
 **organization_fields** | **str**| Any valid value that the [nested organization field resource](/cloud/trello/guides/rest-api/nested-resources/) accepts. | [optional] [default to displayName]
 **board_fields** | **str**| Any valid value that the [nested board resource](/cloud/trello/guides/rest-api/nested-resources/) accepts. | [optional] [default to name]

### Return type

[**list[Member]**](Member.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enterprises_id_members_idmember**
> Member get_enterprises_id_members_idmember(id, id_member, fields=fields, organization_fields=organization_fields, board_fields=board_fields)

Get a Member of Enterprise

Get a specific member of an enterprise by ID.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the enterprise to retrieve.
id_member = trello_api_client.TrelloID() # TrelloID | An ID of a member resource.
fields = 'avatarHash, fullName, initials, username' # str | A comma separated list of any valid values that the [nested member field resource]() accepts. (optional) (default to avatarHash, fullName, initials, username)
organization_fields = 'displayName' # str | Any valid value that the [nested organization field resource](/cloud/trello/guides/rest-api/nested-resources/) accepts. (optional) (default to displayName)
board_fields = 'name' # str | Any valid value that the [nested board resource](/cloud/trello/guides/rest-api/nested-resources/) accepts. (optional) (default to name)

try:
    # Get a Member of Enterprise
    api_response = api_instance.get_enterprises_id_members_idmember(id, id_member, fields=fields, organization_fields=organization_fields, board_fields=board_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_enterprises_id_members_idmember: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the enterprise to retrieve. | 
 **id_member** | [**TrelloID**](.md)| An ID of a member resource. | 
 **fields** | **str**| A comma separated list of any valid values that the [nested member field resource]() accepts. | [optional] [default to avatarHash, fullName, initials, username]
 **organization_fields** | **str**| Any valid value that the [nested organization field resource](/cloud/trello/guides/rest-api/nested-resources/) accepts. | [optional] [default to displayName]
 **board_fields** | **str**| Any valid value that the [nested board resource](/cloud/trello/guides/rest-api/nested-resources/) accepts. | [optional] [default to name]

### Return type

[**Member**](Member.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enterprises_id_organizations_bulk_id_organizations**
> get_enterprises_id_organizations_bulk_id_organizations(id, id_organizations)

Bulk accept a set of organizations to an Enterprise.

Accept an array of organizations to an enterprise.   NOTE: For enterprises that have opted in to user management via AdminHub, this endpoint will result in organizations being added to the enterprise asynchronously. A 200 response only indicates receipt of the request, it does not indicate successful addition to the enterprise.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the enterprise to retrieve.
id_organizations = NULL # list[object] | An array of IDs of the organizations to be removed from the enterprise.

try:
    # Bulk accept a set of organizations to an Enterprise.
    api_instance.get_enterprises_id_organizations_bulk_id_organizations(id, id_organizations)
except ApiException as e:
    print("Exception when calling DefaultApi->get_enterprises_id_organizations_bulk_id_organizations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the enterprise to retrieve. | 
 **id_organizations** | [**list[object]**](object.md)| An array of IDs of the organizations to be removed from the enterprise. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enterprises_id_pending_organizations**
> list[PendingOrganizations] get_enterprises_id_pending_organizations(id, active_since=active_since, inactive_since=inactive_since)

Get PendingOrganizations of an Enterprise

Get the Workspaces that are pending for the enterprise by ID.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the enterprise to retrieve
active_since = 'active_since_example' # str | Date in YYYY-MM-DD format indicating the date to search up to for activeness of workspace (optional)
inactive_since = 'inactive_since_example' # str | Date in YYYY-MM-DD format indicating the date to search up to for inactiveness of workspace (optional)

try:
    # Get PendingOrganizations of an Enterprise
    api_response = api_instance.get_enterprises_id_pending_organizations(id, active_since=active_since, inactive_since=inactive_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_enterprises_id_pending_organizations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the enterprise to retrieve | 
 **active_since** | **str**| Date in YYYY-MM-DD format indicating the date to search up to for activeness of workspace | [optional] 
 **inactive_since** | **str**| Date in YYYY-MM-DD format indicating the date to search up to for inactiveness of workspace | [optional] 

### Return type

[**list[PendingOrganizations]**](PendingOrganizations.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enterprises_id_signupurl**
> InlineResponse200 get_enterprises_id_signupurl(id, authenticate=authenticate, confirmation_accepted=confirmation_accepted, return_url=return_url, tos_accepted=tos_accepted)

Get signupUrl for Enterprise

Get the signup URL for an enterprise.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the enterprise to retrieve.
authenticate = false # bool |  (optional) (default to false)
confirmation_accepted = false # bool |  (optional) (default to false)
return_url = 'return_url_example' # str | Any valid URL. (optional)
tos_accepted = false # bool | Designates whether the user has seen/consented to the Trello ToS prior to being redirected to the enterprise signup page/their IdP. (optional) (default to false)

try:
    # Get signupUrl for Enterprise
    api_response = api_instance.get_enterprises_id_signupurl(id, authenticate=authenticate, confirmation_accepted=confirmation_accepted, return_url=return_url, tos_accepted=tos_accepted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_enterprises_id_signupurl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the enterprise to retrieve. | 
 **authenticate** | **bool**|  | [optional] [default to false]
 **confirmation_accepted** | **bool**|  | [optional] [default to false]
 **return_url** | **str**| Any valid URL. | [optional] 
 **tos_accepted** | **bool**| Designates whether the user has seen/consented to the Trello ToS prior to being redirected to the enterprise signup page/their IdP. | [optional] [default to false]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enterprises_id_transferrable_bulk_id_organizations**
> list[object] get_enterprises_id_transferrable_bulk_id_organizations(id, id_organizations)

Get a bulk list of organizations that can be transferred to an enterprise.

Get a list of organizations that can be transferred to an enterprise when given a bulk list of organizations.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the Enterprise to retrieve.
id_organizations = NULL # list[object] | An array of IDs of an Organization resource.

try:
    # Get a bulk list of organizations that can be transferred to an enterprise.
    api_response = api_instance.get_enterprises_id_transferrable_bulk_id_organizations(id, id_organizations)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_enterprises_id_transferrable_bulk_id_organizations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the Enterprise to retrieve. | 
 **id_organizations** | [**list[object]**](object.md)| An array of IDs of an Organization resource. | 

### Return type

**list[object]**

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enterprises_id_transferrable_organization_id_organization**
> TransferrableOrganization get_enterprises_id_transferrable_organization_id_organization(id, id_organization)

Get whether an organization can be transferred to an enterprise.

Get whether an organization can be transferred to an enterprise.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the Enterprise to retrieve.
id_organization = trello_api_client.TrelloID() # TrelloID | An ID of an Organization resource.

try:
    # Get whether an organization can be transferred to an enterprise.
    api_response = api_instance.get_enterprises_id_transferrable_organization_id_organization(id, id_organization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_enterprises_id_transferrable_organization_id_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the Enterprise to retrieve. | 
 **id_organization** | [**TrelloID**](.md)| An ID of an Organization resource. | 

### Return type

[**TransferrableOrganization**](TransferrableOrganization.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_labels_id**
> get_labels_id(id, fields=fields)

Get a Label

Get information about a single Label.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Label
fields = 'all' # str | all or a comma-separated list of [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional) (default to all)

try:
    # Get a Label
    api_instance.get_labels_id(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->get_labels_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Label | 
 **fields** | **str**| all or a comma-separated list of [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] [default to all]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lists_id**
> get_lists_id(id, fields=fields)

Get a List

Get information about a List

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the list
fields = 'name,closed,idBoard,pos' # str | `all` or a comma separated list of List field names. (optional) (default to name,closed,idBoard,pos)

try:
    # Get a List
    api_instance.get_lists_id(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->get_lists_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the list | 
 **fields** | **str**| &#x60;all&#x60; or a comma separated list of List field names. | [optional] [default to name,closed,idBoard,pos]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lists_id_actions**
> get_lists_id_actions(id, filter=filter)

Get Actions for a List

Get the Actions on a List

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the list
filter = 'filter_example' # str | A comma-separated list of [action types](https://developer.atlassian.com/cloud/trello/guides/rest-api/action-types/). (optional)

try:
    # Get Actions for a List
    api_instance.get_lists_id_actions(id, filter=filter)
except ApiException as e:
    print("Exception when calling DefaultApi->get_lists_id_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the list | 
 **filter** | **str**| A comma-separated list of [action types](https://developer.atlassian.com/cloud/trello/guides/rest-api/action-types/). | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lists_id_board**
> get_lists_id_board(id, fields=fields)

Get the Board a List is on

Get the board a list is on

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the list
fields = 'all' # str | `all` or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/#board-object) (optional) (default to all)

try:
    # Get the Board a List is on
    api_instance.get_lists_id_board(id, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->get_lists_id_board: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the list | 
 **fields** | **str**| &#x60;all&#x60; or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/#board-object) | [optional] [default to all]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lists_id_cards**
> list[Card] get_lists_id_cards(id)

Get Cards in a List

List the cards in a list

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the list

try:
    # Get Cards in a List
    api_response = api_instance.get_lists_id_cards(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_lists_id_cards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the list | 

### Return type

[**list[Card]**](Card.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_id_actions**
> list[object] get_members_id_actions(id, filter=filter)

Get a Member's Actions

List the actions for a member

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member
filter = 'filter_example' # str | A comma-separated list of [action types](https://developer.atlassian.com/cloud/trello/guides/rest-api/action-types/). (optional)

try:
    # Get a Member's Actions
    api_response = api_instance.get_members_id_actions(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_members_id_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 
 **filter** | **str**| A comma-separated list of [action types](https://developer.atlassian.com/cloud/trello/guides/rest-api/action-types/). | [optional] 

### Return type

**list[object]**

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_id_boardbackgrounds**
> list[object] get_members_id_boardbackgrounds(id, filter=filter)

Get Member's custom Board backgrounds

Get a member's custom board backgrounds

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member
filter = 'all' # str | One of: `all`, `custom`, `default`, `none`, `premium` (optional) (default to all)

try:
    # Get Member's custom Board backgrounds
    api_response = api_instance.get_members_id_boardbackgrounds(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_members_id_boardbackgrounds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 
 **filter** | **str**| One of: &#x60;all&#x60;, &#x60;custom&#x60;, &#x60;default&#x60;, &#x60;none&#x60;, &#x60;premium&#x60; | [optional] [default to all]

### Return type

**list[object]**

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_id_boardbackgrounds_idbackground**
> BoardBackground get_members_id_boardbackgrounds_idbackground(id, id_background, fields=fields)

Get a boardBackground of a Member

Get a member's board background

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member
id_background = trello_api_client.TrelloID() # TrelloID | The ID of the board background
fields = 'all' # str | `all` or a comma-separated list of: `brightness`, `fullSizeUrl`, `scaled`, `tile` (optional) (default to all)

try:
    # Get a boardBackground of a Member
    api_response = api_instance.get_members_id_boardbackgrounds_idbackground(id, id_background, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_members_id_boardbackgrounds_idbackground: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 
 **id_background** | [**TrelloID**](.md)| The ID of the board background | 
 **fields** | **str**| &#x60;all&#x60; or a comma-separated list of: &#x60;brightness&#x60;, &#x60;fullSizeUrl&#x60;, &#x60;scaled&#x60;, &#x60;tile&#x60; | [optional] [default to all]

### Return type

[**BoardBackground**](BoardBackground.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_id_boards**
> list[Board] get_members_id_boards(id, filter=filter, fields=fields, lists=lists, organization=organization, organization_fields=organization_fields)

Get Boards that Member belongs to

Lists the boards that the user is a member of.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member
filter = 'all' # str | `all` or a comma-separated list of: `closed`, `members`, `open`, `organization`, `public`, `starred` (optional) (default to all)
fields = trello_api_client.BoardFields() # BoardFields | `all` or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional)
lists = 'none' # str | Which lists to include with the boards. One of: `all`, `closed`, `none`, `open` (optional) (default to none)
organization = false # bool | Whether to include the Organization object with the Boards (optional) (default to false)
organization_fields = trello_api_client.OrganizationFields() # OrganizationFields | `all` or a comma-separated list of organization [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional)

try:
    # Get Boards that Member belongs to
    api_response = api_instance.get_members_id_boards(id, filter=filter, fields=fields, lists=lists, organization=organization, organization_fields=organization_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_members_id_boards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 
 **filter** | **str**| &#x60;all&#x60; or a comma-separated list of: &#x60;closed&#x60;, &#x60;members&#x60;, &#x60;open&#x60;, &#x60;organization&#x60;, &#x60;public&#x60;, &#x60;starred&#x60; | [optional] [default to all]
 **fields** | [**BoardFields**](.md)| &#x60;all&#x60; or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] 
 **lists** | **str**| Which lists to include with the boards. One of: &#x60;all&#x60;, &#x60;closed&#x60;, &#x60;none&#x60;, &#x60;open&#x60; | [optional] [default to none]
 **organization** | **bool**| Whether to include the Organization object with the Boards | [optional] [default to false]
 **organization_fields** | [**OrganizationFields**](.md)| &#x60;all&#x60; or a comma-separated list of organization [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] 

### Return type

[**list[Board]**](Board.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_id_boardsinvited**
> list[Board] get_members_id_boardsinvited(id, fields=fields)

Get Boards the Member has been invited to

Get the boards the member has been invited to

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member
fields = trello_api_client.BoardFields() # BoardFields | `all` or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional)

try:
    # Get Boards the Member has been invited to
    api_response = api_instance.get_members_id_boardsinvited(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_members_id_boardsinvited: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 
 **fields** | [**BoardFields**](.md)| &#x60;all&#x60; or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] 

### Return type

[**list[Board]**](Board.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_id_boardstars**
> get_members_id_boardstars(id)

Get a Member's boardStars

List a member's board stars

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member

try:
    # Get a Member's boardStars
    api_instance.get_members_id_boardstars(id)
except ApiException as e:
    print("Exception when calling DefaultApi->get_members_id_boardstars: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_id_boardstars_idstar**
> BoardStars get_members_id_boardstars_idstar(id, id_star)

Get a boardStar of Member

Get a specific boardStar

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member
id_star = trello_api_client.TrelloID() # TrelloID | The ID of the board star

try:
    # Get a boardStar of Member
    api_response = api_instance.get_members_id_boardstars_idstar(id, id_star)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_members_id_boardstars_idstar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 
 **id_star** | [**TrelloID**](.md)| The ID of the board star | 

### Return type

[**BoardStars**](BoardStars.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_id_cards**
> list[Card] get_members_id_cards(id, filter=filter)

Get Cards the Member is on

Gets the cards a member is on

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member
filter = 'visible' # str | One of: `all`, `closed`, `none`, `open`, `visible` (optional) (default to visible)

try:
    # Get Cards the Member is on
    api_response = api_instance.get_members_id_cards(id, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_members_id_cards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 
 **filter** | **str**| One of: &#x60;all&#x60;, &#x60;closed&#x60;, &#x60;none&#x60;, &#x60;open&#x60;, &#x60;visible&#x60; | [optional] [default to visible]

### Return type

[**list[Card]**](Card.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_id_customboardbackgrounds**
> list[BoardBackground] get_members_id_customboardbackgrounds(id)

Get a Member's custom Board Backgrounds

Get a member's custom board backgrounds

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member

try:
    # Get a Member's custom Board Backgrounds
    api_response = api_instance.get_members_id_customboardbackgrounds(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_members_id_customboardbackgrounds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 

### Return type

[**list[BoardBackground]**](BoardBackground.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_id_customboardbackgrounds_idbackground**
> BoardBackground get_members_id_customboardbackgrounds_idbackground(id, id_background)

Get custom Board Background of Member

Get a specific custom board background

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.Id2() # Id2 | The ID or username of the member
id_background = trello_api_client.TrelloID() # TrelloID | The ID of the custom background

try:
    # Get custom Board Background of Member
    api_response = api_instance.get_members_id_customboardbackgrounds_idbackground(id, id_background)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_members_id_customboardbackgrounds_idbackground: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id2**](.md)| The ID or username of the member | 
 **id_background** | [**TrelloID**](.md)| The ID of the custom background | 

### Return type

[**BoardBackground**](BoardBackground.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_id_customemoji**
> list[CustomEmoji] get_members_id_customemoji(id)

Get a Member's customEmojis

Get a Member's uploaded custom Emojis

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member

try:
    # Get a Member's customEmojis
    api_response = api_instance.get_members_id_customemoji(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_members_id_customemoji: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 

### Return type

[**list[CustomEmoji]**](CustomEmoji.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_id_customstickers**
> list[CustomSticker] get_members_id_customstickers(id)

Get Member's custom Stickers

Get a Member's uploaded stickers

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member

try:
    # Get Member's custom Stickers
    api_response = api_instance.get_members_id_customstickers(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_members_id_customstickers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 

### Return type

[**list[CustomSticker]**](CustomSticker.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_id_customstickers_idsticker**
> CustomSticker get_members_id_customstickers_idsticker(id, id_sticker, fields=fields)

Get a Member's custom Sticker

Get a Member's custom Sticker

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member
id_sticker = trello_api_client.TrelloID() # TrelloID | The ID of the uploaded sticker
fields = 'all' # str | `all` or a comma-separated list of `scaled`, `url` (optional) (default to all)

try:
    # Get a Member's custom Sticker
    api_response = api_instance.get_members_id_customstickers_idsticker(id, id_sticker, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_members_id_customstickers_idsticker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 
 **id_sticker** | [**TrelloID**](.md)| The ID of the uploaded sticker | 
 **fields** | **str**| &#x60;all&#x60; or a comma-separated list of &#x60;scaled&#x60;, &#x60;url&#x60; | [optional] [default to all]

### Return type

[**CustomSticker**](CustomSticker.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_id_field**
> InlineResponse2001 get_members_id_field(id, field)

Get a field on a Member

Get a particular property of a member

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member
field = trello_api_client.MemberFields() # MemberFields | One of the member [fields](/cloud/trello/guides/rest-api/object-definitions/)

try:
    # Get a field on a Member
    api_response = api_instance.get_members_id_field(id, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_members_id_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 
 **field** | [**MemberFields**](.md)| One of the member [fields](/cloud/trello/guides/rest-api/object-definitions/) | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_id_notification_channel_settings**
> list[NotificationChannelSettings] get_members_id_notification_channel_settings(id)

Get a Member's notification channel settings

Get a member's notification channel settings

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.Id3() # Id3 | The ID or username of the member

try:
    # Get a Member's notification channel settings
    api_response = api_instance.get_members_id_notification_channel_settings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_members_id_notification_channel_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id3**](.md)| The ID or username of the member | 

### Return type

[**list[NotificationChannelSettings]**](NotificationChannelSettings.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_id_notification_channel_settings_channel**
> NotificationChannelSettings get_members_id_notification_channel_settings_channel(id, channel)

Get blocked notification keys of Member on this channel

Get blocked notification keys of Member on a specific channel

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.Id4() # Id4 | The ID or username of the member
channel = trello_api_client.Channel() # Channel | Channel to block notifications on

try:
    # Get blocked notification keys of Member on this channel
    api_response = api_instance.get_members_id_notification_channel_settings_channel(id, channel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_members_id_notification_channel_settings_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id4**](.md)| The ID or username of the member | 
 **channel** | [**Channel**](.md)| Channel to block notifications on | 

### Return type

[**NotificationChannelSettings**](NotificationChannelSettings.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_id_notifications**
> list[Notification] get_members_id_notifications(id, entities=entities, display=display, filter=filter, read_filter=read_filter, fields=fields, limit=limit, page=page, before=before, since=since, member_creator=member_creator, member_creator_fields=member_creator_fields)

Get Member's Notifications

Get a member's notifications

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member
entities = false # bool |  (optional) (default to false)
display = false # bool |  (optional) (default to false)
filter = 'all' # str |  (optional) (default to all)
read_filter = 'all' # str | One of: `all`, `read`, `unread` (optional) (default to all)
fields = 'all' # str | `all` or a comma-separated list of notification [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional) (default to all)
limit = 56 # int | Max 1000 (optional)
page = 56 # int | Max 100 (optional)
before = 'before_example' # str | A notification ID (optional)
since = 'since_example' # str | A notification ID (optional)
member_creator = true # bool |  (optional) (default to true)
member_creator_fields = 'avatarHash,fullName,initials,username' # str | `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional) (default to avatarHash,fullName,initials,username)

try:
    # Get Member's Notifications
    api_response = api_instance.get_members_id_notifications(id, entities=entities, display=display, filter=filter, read_filter=read_filter, fields=fields, limit=limit, page=page, before=before, since=since, member_creator=member_creator, member_creator_fields=member_creator_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_members_id_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 
 **entities** | **bool**|  | [optional] [default to false]
 **display** | **bool**|  | [optional] [default to false]
 **filter** | **str**|  | [optional] [default to all]
 **read_filter** | **str**| One of: &#x60;all&#x60;, &#x60;read&#x60;, &#x60;unread&#x60; | [optional] [default to all]
 **fields** | **str**| &#x60;all&#x60; or a comma-separated list of notification [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] [default to all]
 **limit** | **int**| Max 1000 | [optional] 
 **page** | **int**| Max 100 | [optional] 
 **before** | **str**| A notification ID | [optional] 
 **since** | **str**| A notification ID | [optional] 
 **member_creator** | **bool**|  | [optional] [default to true]
 **member_creator_fields** | **str**| &#x60;all&#x60; or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] [default to avatarHash,fullName,initials,username]

### Return type

[**list[Notification]**](Notification.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_id_organizations**
> list[Organization] get_members_id_organizations(id, filter=filter, fields=fields, paid_account=paid_account)

Get Member's Organizations

Get a member's Workspaces

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member
filter = 'all' # str | One of: `all`, `members`, `none`, `public` (Note: `members` filters to only private Workspaces) (optional) (default to all)
fields = trello_api_client.OrganizationFields() # OrganizationFields | `all` or a comma-separated list of organization [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional)
paid_account = false # bool | Whether or not to include paid account information in the returned workspace object (optional) (default to false)

try:
    # Get Member's Organizations
    api_response = api_instance.get_members_id_organizations(id, filter=filter, fields=fields, paid_account=paid_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_members_id_organizations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 
 **filter** | **str**| One of: &#x60;all&#x60;, &#x60;members&#x60;, &#x60;none&#x60;, &#x60;public&#x60; (Note: &#x60;members&#x60; filters to only private Workspaces) | [optional] [default to all]
 **fields** | [**OrganizationFields**](.md)| &#x60;all&#x60; or a comma-separated list of organization [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] 
 **paid_account** | **bool**| Whether or not to include paid account information in the returned workspace object | [optional] [default to false]

### Return type

[**list[Organization]**](Organization.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_id_organizationsinvited**
> list[Organization] get_members_id_organizationsinvited(id, fields=fields)

Get Organizations a Member has been invited to

Get a member's Workspaces they have been invited to

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member
fields = trello_api_client.OrganizationFields() # OrganizationFields | `all` or a comma-separated list of organization [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional)

try:
    # Get Organizations a Member has been invited to
    api_response = api_instance.get_members_id_organizationsinvited(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_members_id_organizationsinvited: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 
 **fields** | [**OrganizationFields**](.md)| &#x60;all&#x60; or a comma-separated list of organization [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] 

### Return type

[**list[Organization]**](Organization.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_id_savedsearches**
> list[SavedSearch] get_members_id_savedsearches(id)

Get Member's saved searched

List the saved searches of a Member

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member

try:
    # Get Member's saved searched
    api_response = api_instance.get_members_id_savedsearches(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_members_id_savedsearches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 

### Return type

[**list[SavedSearch]**](SavedSearch.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_id_savedsearches_idsearch**
> SavedSearch get_members_id_savedsearches_idsearch(id, id_search)

Get a saved search

Get a saved search

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
id_search = 'id_search_example' # str | The ID of the saved search to delete

try:
    # Get a saved search
    api_response = api_instance.get_members_id_savedsearches_idsearch(id, id_search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_members_id_savedsearches_idsearch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **id_search** | **str**| The ID of the saved search to delete | 

### Return type

[**SavedSearch**](SavedSearch.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_id_tokens**
> list[Token] get_members_id_tokens(id, webhooks=webhooks)

Get Member's Tokens

List a members app tokens

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member
webhooks = false # bool | Whether to include webhooks (optional) (default to false)

try:
    # Get Member's Tokens
    api_response = api_instance.get_members_id_tokens(id, webhooks=webhooks)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_members_id_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 
 **webhooks** | **bool**| Whether to include webhooks | [optional] [default to false]

### Return type

[**list[Token]**](Token.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_membersid**
> InlineResponse2001 get_membersid(id, actions=actions, boards=boards, board_backgrounds=board_backgrounds, boards_invited=boards_invited, boards_invited_fields=boards_invited_fields, board_stars=board_stars, cards=cards, custom_board_backgrounds=custom_board_backgrounds, custom_emoji=custom_emoji, custom_stickers=custom_stickers, fields=fields, notifications=notifications, organizations=organizations, organization_fields=organization_fields, organization_paid_account=organization_paid_account, organizations_invited=organizations_invited, organizations_invited_fields=organizations_invited_fields, paid_account=paid_account, saved_searches=saved_searches, tokens=tokens)

Get a Member

Get a member

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.Id() # Id | The ID or username of the member
actions = 'actions_example' # str | See the [Actions Nested Resource](/cloud/trello/guides/rest-api/nested-resources/#actions-nested-resource) (optional)
boards = 'boards_example' # str | See the [Boards Nested Resource](/cloud/trello/guides/rest-api/nested-resources/#boards-nested-resource) (optional)
board_backgrounds = 'none' # str | One of: `all`, `custom`, `default`, `none`, `premium` (optional) (default to none)
boards_invited = 'boards_invited_example' # str | `all` or a comma-separated list of: closed, members, open, organization, pinned, public, starred, unpinned (optional)
boards_invited_fields = trello_api_client.BoardFields() # BoardFields | `all` or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional)
board_stars = false # bool | Whether to return the boardStars or not (optional) (default to false)
cards = 'none' # str | See the [Cards Nested Resource](/cloud/trello/guides/rest-api/nested-resources/#cards-nested-resource) for additional options (optional) (default to none)
custom_board_backgrounds = 'none' # str | `all` or `none` (optional) (default to none)
custom_emoji = 'none' # str | `all` or `none` (optional) (default to none)
custom_stickers = 'none' # str | `all` or `none` (optional) (default to none)
fields = trello_api_client.MemberFields() # MemberFields | `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional)
notifications = 'notifications_example' # str | See the [Notifications Nested Resource](/cloud/trello/guides/rest-api/nested-resources/#notifications-nested-resource) (optional)
organizations = 'none' # str | One of: `all`, `members`, `none`, `public` (optional) (default to none)
organization_fields = trello_api_client.OrganizationFields() # OrganizationFields | `all` or a comma-separated list of organization [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional)
organization_paid_account = false # bool | Whether or not to include paid account information in the returned workspace object (optional) (default to false)
organizations_invited = 'none' # str | One of: `all`, `members`, `none`, `public` (optional) (default to none)
organizations_invited_fields = trello_api_client.OrganizationFields() # OrganizationFields | `all` or a comma-separated list of organization [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional)
paid_account = false # bool | Whether or not to include paid account information in the returned member object (optional) (default to false)
saved_searches = false # bool |  (optional) (default to false)
tokens = 'none' # str | `all` or `none` (optional) (default to none)

try:
    # Get a Member
    api_response = api_instance.get_membersid(id, actions=actions, boards=boards, board_backgrounds=board_backgrounds, boards_invited=boards_invited, boards_invited_fields=boards_invited_fields, board_stars=board_stars, cards=cards, custom_board_backgrounds=custom_board_backgrounds, custom_emoji=custom_emoji, custom_stickers=custom_stickers, fields=fields, notifications=notifications, organizations=organizations, organization_fields=organization_fields, organization_paid_account=organization_paid_account, organizations_invited=organizations_invited, organizations_invited_fields=organizations_invited_fields, paid_account=paid_account, saved_searches=saved_searches, tokens=tokens)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_membersid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id**](.md)| The ID or username of the member | 
 **actions** | **str**| See the [Actions Nested Resource](/cloud/trello/guides/rest-api/nested-resources/#actions-nested-resource) | [optional] 
 **boards** | **str**| See the [Boards Nested Resource](/cloud/trello/guides/rest-api/nested-resources/#boards-nested-resource) | [optional] 
 **board_backgrounds** | **str**| One of: &#x60;all&#x60;, &#x60;custom&#x60;, &#x60;default&#x60;, &#x60;none&#x60;, &#x60;premium&#x60; | [optional] [default to none]
 **boards_invited** | **str**| &#x60;all&#x60; or a comma-separated list of: closed, members, open, organization, pinned, public, starred, unpinned | [optional] 
 **boards_invited_fields** | [**BoardFields**](.md)| &#x60;all&#x60; or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] 
 **board_stars** | **bool**| Whether to return the boardStars or not | [optional] [default to false]
 **cards** | **str**| See the [Cards Nested Resource](/cloud/trello/guides/rest-api/nested-resources/#cards-nested-resource) for additional options | [optional] [default to none]
 **custom_board_backgrounds** | **str**| &#x60;all&#x60; or &#x60;none&#x60; | [optional] [default to none]
 **custom_emoji** | **str**| &#x60;all&#x60; or &#x60;none&#x60; | [optional] [default to none]
 **custom_stickers** | **str**| &#x60;all&#x60; or &#x60;none&#x60; | [optional] [default to none]
 **fields** | [**MemberFields**](.md)| &#x60;all&#x60; or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] 
 **notifications** | **str**| See the [Notifications Nested Resource](/cloud/trello/guides/rest-api/nested-resources/#notifications-nested-resource) | [optional] 
 **organizations** | **str**| One of: &#x60;all&#x60;, &#x60;members&#x60;, &#x60;none&#x60;, &#x60;public&#x60; | [optional] [default to none]
 **organization_fields** | [**OrganizationFields**](.md)| &#x60;all&#x60; or a comma-separated list of organization [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] 
 **organization_paid_account** | **bool**| Whether or not to include paid account information in the returned workspace object | [optional] [default to false]
 **organizations_invited** | **str**| One of: &#x60;all&#x60;, &#x60;members&#x60;, &#x60;none&#x60;, &#x60;public&#x60; | [optional] [default to none]
 **organizations_invited_fields** | [**OrganizationFields**](.md)| &#x60;all&#x60; or a comma-separated list of organization [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] 
 **paid_account** | **bool**| Whether or not to include paid account information in the returned member object | [optional] [default to false]
 **saved_searches** | **bool**|  | [optional] [default to false]
 **tokens** | **str**| &#x60;all&#x60; or &#x60;none&#x60; | [optional] [default to none]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notifications_id**
> InlineResponse2002 get_notifications_id(id, board=board, board_fields=board_fields, card=card, card_fields=card_fields, display=display, entities=entities, fields=fields, list=list, member=member, member_fields=member_fields, member_creator=member_creator, member_creator_fields=member_creator_fields, organization=organization, organization_fields=organization_fields)

Get a Notification

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the notification
board = false # bool | Whether to include the board object (optional) (default to false)
board_fields = trello_api_client.BoardFields() # BoardFields | `all` or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional)
card = false # bool | Whether to include the card object (optional) (default to false)
card_fields = trello_api_client.CardFields() # CardFields | `all` or a comma-separated list of card [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional)
display = false # bool | Whether to include the display object with the results (optional) (default to false)
entities = false # bool | Whether to include the entities object with the results (optional) (default to false)
fields = trello_api_client.NotificationFields() # NotificationFields | `all` or a comma-separated list of notification [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional)
list = false # bool | Whether to include the list object (optional) (default to false)
member = true # bool | Whether to include the member object (optional) (default to true)
member_fields = trello_api_client.MemberFields() # MemberFields | `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional)
member_creator = true # bool | Whether to include the member object of the creator (optional) (default to true)
member_creator_fields = trello_api_client.MemberFields() # MemberFields | `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional)
organization = false # bool | Whether to include the organization object (optional) (default to false)
organization_fields = trello_api_client.OrganizationFields() # OrganizationFields | `all` or a comma-separated list of organization [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional)

try:
    # Get a Notification
    api_response = api_instance.get_notifications_id(id, board=board, board_fields=board_fields, card=card, card_fields=card_fields, display=display, entities=entities, fields=fields, list=list, member=member, member_fields=member_fields, member_creator=member_creator, member_creator_fields=member_creator_fields, organization=organization, organization_fields=organization_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_notifications_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the notification | 
 **board** | **bool**| Whether to include the board object | [optional] [default to false]
 **board_fields** | [**BoardFields**](.md)| &#x60;all&#x60; or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] 
 **card** | **bool**| Whether to include the card object | [optional] [default to false]
 **card_fields** | [**CardFields**](.md)| &#x60;all&#x60; or a comma-separated list of card [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] 
 **display** | **bool**| Whether to include the display object with the results | [optional] [default to false]
 **entities** | **bool**| Whether to include the entities object with the results | [optional] [default to false]
 **fields** | [**NotificationFields**](.md)| &#x60;all&#x60; or a comma-separated list of notification [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] 
 **list** | **bool**| Whether to include the list object | [optional] [default to false]
 **member** | **bool**| Whether to include the member object | [optional] [default to true]
 **member_fields** | [**MemberFields**](.md)| &#x60;all&#x60; or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] 
 **member_creator** | **bool**| Whether to include the member object of the creator | [optional] [default to true]
 **member_creator_fields** | [**MemberFields**](.md)| &#x60;all&#x60; or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] 
 **organization** | **bool**| Whether to include the organization object | [optional] [default to false]
 **organization_fields** | [**OrganizationFields**](.md)| &#x60;all&#x60; or a comma-separated list of organization [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notifications_id_board**
> InlineResponse2003 get_notifications_id_board(id, fields=fields)

Get the Board a Notification is on

Get the board a notification is associated with

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the notification
fields = trello_api_client.BoardFields() # BoardFields | `all` or a comma-separated list of board[fields](/cloud/trello/guides/rest-api/object-definitions/) (optional)

try:
    # Get the Board a Notification is on
    api_response = api_instance.get_notifications_id_board(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_notifications_id_board: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the notification | 
 **fields** | [**BoardFields**](.md)| &#x60;all&#x60; or a comma-separated list of board[fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notifications_id_card**
> InlineResponse2004 get_notifications_id_card(id, fields=fields)

Get the Card a Notification is on

Get the card a notification is associated with

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the notification
fields = trello_api_client.CardFields() # CardFields | `all` or a comma-separated list of card [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional)

try:
    # Get the Card a Notification is on
    api_response = api_instance.get_notifications_id_card(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_notifications_id_card: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the notification | 
 **fields** | [**CardFields**](.md)| &#x60;all&#x60; or a comma-separated list of card [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notifications_id_field**
> InlineResponse2002 get_notifications_id_field(id, field)

Get a field of a Notification

Get a specific property of a notification

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the notification
field = trello_api_client.NotificationFields() # NotificationFields | A notification [field](/cloud/trello/guides/rest-api/object-definitions/)

try:
    # Get a field of a Notification
    api_response = api_instance.get_notifications_id_field(id, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_notifications_id_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the notification | 
 **field** | [**NotificationFields**](.md)| A notification [field](/cloud/trello/guides/rest-api/object-definitions/) | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notifications_id_list**
> InlineResponse2005 get_notifications_id_list(id, fields=fields)

Get the List a Notification is on

Get the list a notification is associated with

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the notification
fields = trello_api_client.ListFields() # ListFields | `all` or a comma-separated list of list [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional)

try:
    # Get the List a Notification is on
    api_response = api_instance.get_notifications_id_list(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_notifications_id_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the notification | 
 **fields** | [**ListFields**](.md)| &#x60;all&#x60; or a comma-separated list of list [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notifications_id_membercreator**
> InlineResponse2001 get_notifications_id_membercreator(id, fields=fields)

Get the Member who created the Notification

Get the member who created the notification

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the notification
fields = trello_api_client.MemberFields() # MemberFields | `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional)

try:
    # Get the Member who created the Notification
    api_response = api_instance.get_notifications_id_membercreator(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_notifications_id_membercreator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the notification | 
 **fields** | [**MemberFields**](.md)| &#x60;all&#x60; or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notifications_id_organization**
> InlineResponse2006 get_notifications_id_organization(id, fields=fields)

Get a Notification's associated Organization

Get the organization a notification is associated with

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the notification
fields = trello_api_client.OrganizationFields() # OrganizationFields | `all` or a comma-separated list of organization [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional)

try:
    # Get a Notification's associated Organization
    api_response = api_instance.get_notifications_id_organization(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_notifications_id_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the notification | 
 **fields** | [**OrganizationFields**](.md)| &#x60;all&#x60; or a comma-separated list of organization [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_id**
> Organization get_organizations_id(id)

Get an Organization

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or name of the Organization

try:
    # Get an Organization
    api_response = api_instance.get_organizations_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_organizations_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or name of the Organization | 

### Return type

[**Organization**](Organization.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_id_actions**
> list[Action] get_organizations_id_actions(id)

Get Actions for Organization

List the actions on a Workspace

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or name of the organization

try:
    # Get Actions for Organization
    api_response = api_instance.get_organizations_id_actions(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_organizations_id_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or name of the organization | 

### Return type

[**list[Action]**](Action.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_id_boards**
> list[object] get_organizations_id_boards(id, filter=filter, fields=fields)

Get Boards in an Organization

List the boards in a Workspace

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or name of the organization
filter = 'all' # str | `all` or a comma-separated list of: `open`, `closed`, `members`, `organization`, `public` (optional) (default to all)
fields = trello_api_client.BoardFields() # BoardFields | `all` or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional)

try:
    # Get Boards in an Organization
    api_response = api_instance.get_organizations_id_boards(id, filter=filter, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_organizations_id_boards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or name of the organization | 
 **filter** | **str**| &#x60;all&#x60; or a comma-separated list of: &#x60;open&#x60;, &#x60;closed&#x60;, &#x60;members&#x60;, &#x60;organization&#x60;, &#x60;public&#x60; | [optional] [default to all]
 **fields** | **BoardFields**| &#x60;all&#x60; or a comma-separated list of board [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] 

### Return type

**list[object]**

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_id_exports**
> list[Export] get_organizations_id_exports(id)

Retrieve Organization's Exports

Retrieve the exports that exist for the given organization

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or name of the Workspace

try:
    # Retrieve Organization's Exports
    api_response = api_instance.get_organizations_id_exports(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_organizations_id_exports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or name of the Workspace | 

### Return type

[**list[Export]**](Export.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_id_field**
> Organization get_organizations_id_field(id, field)

Get field on Organization

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or name of the organization
field = trello_api_client.OrganizationFields() # OrganizationFields | An organization [field](/cloud/trello/guides/rest-api/object-definitions/)

try:
    # Get field on Organization
    api_response = api_instance.get_organizations_id_field(id, field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_organizations_id_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or name of the organization | 
 **field** | [**OrganizationFields**](.md)| An organization [field](/cloud/trello/guides/rest-api/object-definitions/) | 

### Return type

[**Organization**](Organization.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_id_members**
> list[object] get_organizations_id_members(id)

Get the Members of an Organization

List the members in a Workspace

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or name of the Organization

try:
    # Get the Members of an Organization
    api_response = api_instance.get_organizations_id_members(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_organizations_id_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or name of the Organization | 

### Return type

**list[object]**

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_id_memberships**
> list[object] get_organizations_id_memberships(id, filter=filter, member=member)

Get Memberships of an Organization

List the memberships of a Workspace

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or name of the organization
filter = 'all' # str | `all` or a comma-separated list of: `active`, `admin`, `deactivated`, `me`, `normal` (optional) (default to all)
member = false # bool | Whether to include the Member objects with the Memberships (optional) (default to false)

try:
    # Get Memberships of an Organization
    api_response = api_instance.get_organizations_id_memberships(id, filter=filter, member=member)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_organizations_id_memberships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or name of the organization | 
 **filter** | **str**| &#x60;all&#x60; or a comma-separated list of: &#x60;active&#x60;, &#x60;admin&#x60;, &#x60;deactivated&#x60;, &#x60;me&#x60;, &#x60;normal&#x60; | [optional] [default to all]
 **member** | **bool**| Whether to include the Member objects with the Memberships | [optional] [default to false]

### Return type

**list[object]**

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_id_memberships_idmembership**
> InlineResponse2007 get_organizations_id_memberships_idmembership(id, id_membership, member=member)

Get a Membership of an Organization

Get a single Membership for an Organization

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or name of the organization
id_membership = trello_api_client.TrelloID() # TrelloID | The ID of the membership to load
member = false # bool | Whether to include the Member object in the response (optional) (default to false)

try:
    # Get a Membership of an Organization
    api_response = api_instance.get_organizations_id_memberships_idmembership(id, id_membership, member=member)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_organizations_id_memberships_idmembership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or name of the organization | 
 **id_membership** | [**TrelloID**](.md)| The ID of the membership to load | 
 **member** | **bool**| Whether to include the Member object in the response | [optional] [default to false]

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_id_newbillableguests_idboard**
> get_organizations_id_newbillableguests_idboard(id, id_board)

Get Organizations new billable guests

Used to check whether the given board has new billable guests on it.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or name of the organization
id_board = trello_api_client.TrelloID() # TrelloID | The ID of the board to check for new billable guests.

try:
    # Get Organizations new billable guests
    api_instance.get_organizations_id_newbillableguests_idboard(id, id_board)
except ApiException as e:
    print("Exception when calling DefaultApi->get_organizations_id_newbillableguests_idboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or name of the organization | 
 **id_board** | [**TrelloID**](.md)| The ID of the board to check for new billable guests. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_id_plugindata**
> list[object] get_organizations_id_plugindata(id)

Get the pluginData Scoped to Organization

Get organization scoped pluginData on this Workspace

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or name of the organization

try:
    # Get the pluginData Scoped to Organization
    api_response = api_instance.get_organizations_id_plugindata(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_organizations_id_plugindata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or name of the organization | 

### Return type

**list[object]**

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations_id_tags**
> list[object] get_organizations_id_tags(id)

Get Tags of an Organization

List the organization's collections

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.Id6() # Id6 | The ID or name of the Organization

try:
    # Get Tags of an Organization
    api_response = api_instance.get_organizations_id_tags(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_organizations_id_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id6**](.md)| The ID or name of the Organization | 

### Return type

**list[object]**

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugins_id**
> Plugin get_plugins_id(id)

Get a Plugin

Get plugins

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or name of the organization

try:
    # Get a Plugin
    api_response = api_instance.get_plugins_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_plugins_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or name of the organization | 

### Return type

[**Plugin**](Plugin.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plugins_id_compliance_memberprivacy**
> get_plugins_id_compliance_memberprivacy(id)

Get Plugin's Member privacy compliance

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Power-Up

try:
    # Get Plugin's Member privacy compliance
    api_instance.get_plugins_id_compliance_memberprivacy(id)
except ApiException as e:
    print("Exception when calling DefaultApi->get_plugins_id_compliance_memberprivacy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Power-Up | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search**
> list[object] get_search(query, id_boards=id_boards, id_organizations=id_organizations, id_cards=id_cards, model_types=model_types, board_fields=board_fields, boards_limit=boards_limit, board_organization=board_organization, card_fields=card_fields, cards_limit=cards_limit, cards_page=cards_page, card_board=card_board, card_list=card_list, card_members=card_members, card_stickers=card_stickers, card_attachments=card_attachments, organization_fields=organization_fields, organizations_limit=organizations_limit, member_fields=member_fields, members_limit=members_limit, partial=partial)

Search Trello

Find what you're looking for in Trello

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
query = 'query_example' # str | The search query with a length of 1 to 16384 characters
id_boards = trello_api_client.IdBoards() # IdBoards | `mine` or a comma-separated list of Board IDs (optional)
id_organizations = 'id_organizations_example' # str | A comma-separated list of Organization IDs (optional)
id_cards = 'id_cards_example' # str | A comma-separated list of Card IDs (optional)
model_types = 'all' # str | What type or types of Trello objects you want to search. all or a comma-separated list of: `actions`, `boards`, `cards`, `members`, `organizations` (optional) (default to all)
board_fields = 'name,idOrganization' # str | all or a comma-separated list of: `closed`, `dateLastActivity`, `dateLastView`, `desc`, `descData`, `idOrganization`, `invitations`, `invited`, `labelNames`, `memberships`, `name`, `pinned`, `powerUps`, `prefs`, `shortLink`, `shortUrl`, `starred`, `subscribed`, `url` (optional) (default to name,idOrganization)
boards_limit = 10 # int | The maximum number of boards returned. Maximum: 1000 (optional) (default to 10)
board_organization = false # bool | Whether to include the parent organization with board results (optional) (default to false)
card_fields = 'all' # str | all or a comma-separated list of: `badges`, `checkItemStates`, `closed`, `dateLastActivity`, `desc`, `descData`, `due`, `email`, `idAttachmentCover`, `idBoard`, `idChecklists`, `idLabels`, `idList`, `idMembers`, `idMembersVoted`, `idShort`, `labels`, `manualCoverAttachment`, `name`, `pos`, `shortLink`, `shortUrl`, `subscribed`, `url` (optional) (default to all)
cards_limit = 10 # int | The maximum number of cards to return. Maximum: 1000 (optional) (default to 10)
cards_page = 0 # float | The page of results for cards. Maximum: 100 (optional) (default to 0)
card_board = false # bool | Whether to include the parent board with card results (optional) (default to false)
card_list = false # bool | Whether to include the parent list with card results (optional) (default to false)
card_members = false # bool | Whether to include member objects with card results (optional) (default to false)
card_stickers = false # bool | Whether to include sticker objects with card results (optional) (default to false)
card_attachments = 'false' # str | Whether to include attachment objects with card results. A boolean value (true or false) or cover for only card cover attachments. (optional) (default to false)
organization_fields = 'name,displayName' # str | all or a comma-separated list of billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url, website (optional) (default to name,displayName)
organizations_limit = 56 # int | The maximum number of Workspaces to return. Maximum 1000 (optional)
member_fields = 'avatarHash,fullName,initials,username,confirmed' # str | all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url, username (optional) (default to avatarHash,fullName,initials,username,confirmed)
members_limit = 56 # int | The maximum number of members to return. Maximum 1000 (optional)
partial = false # bool | By default, Trello searches for each word in your query against exactly matching words within Member content. Specifying partial to be true means that we will look for content that starts with any of the words in your query.  If you are looking for a Card titled \"My Development Status Report\", by default you would need to search for \"Development\". If you have partial enabled, you will be able to search for \"dev\" but not \"velopment\". (optional) (default to false)

try:
    # Search Trello
    api_response = api_instance.get_search(query, id_boards=id_boards, id_organizations=id_organizations, id_cards=id_cards, model_types=model_types, board_fields=board_fields, boards_limit=boards_limit, board_organization=board_organization, card_fields=card_fields, cards_limit=cards_limit, cards_page=cards_page, card_board=card_board, card_list=card_list, card_members=card_members, card_stickers=card_stickers, card_attachments=card_attachments, organization_fields=organization_fields, organizations_limit=organizations_limit, member_fields=member_fields, members_limit=members_limit, partial=partial)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| The search query with a length of 1 to 16384 characters | 
 **id_boards** | [**IdBoards**](.md)| &#x60;mine&#x60; or a comma-separated list of Board IDs | [optional] 
 **id_organizations** | **str**| A comma-separated list of Organization IDs | [optional] 
 **id_cards** | **str**| A comma-separated list of Card IDs | [optional] 
 **model_types** | **str**| What type or types of Trello objects you want to search. all or a comma-separated list of: &#x60;actions&#x60;, &#x60;boards&#x60;, &#x60;cards&#x60;, &#x60;members&#x60;, &#x60;organizations&#x60; | [optional] [default to all]
 **board_fields** | **str**| all or a comma-separated list of: &#x60;closed&#x60;, &#x60;dateLastActivity&#x60;, &#x60;dateLastView&#x60;, &#x60;desc&#x60;, &#x60;descData&#x60;, &#x60;idOrganization&#x60;, &#x60;invitations&#x60;, &#x60;invited&#x60;, &#x60;labelNames&#x60;, &#x60;memberships&#x60;, &#x60;name&#x60;, &#x60;pinned&#x60;, &#x60;powerUps&#x60;, &#x60;prefs&#x60;, &#x60;shortLink&#x60;, &#x60;shortUrl&#x60;, &#x60;starred&#x60;, &#x60;subscribed&#x60;, &#x60;url&#x60; | [optional] [default to name,idOrganization]
 **boards_limit** | **int**| The maximum number of boards returned. Maximum: 1000 | [optional] [default to 10]
 **board_organization** | **bool**| Whether to include the parent organization with board results | [optional] [default to false]
 **card_fields** | **str**| all or a comma-separated list of: &#x60;badges&#x60;, &#x60;checkItemStates&#x60;, &#x60;closed&#x60;, &#x60;dateLastActivity&#x60;, &#x60;desc&#x60;, &#x60;descData&#x60;, &#x60;due&#x60;, &#x60;email&#x60;, &#x60;idAttachmentCover&#x60;, &#x60;idBoard&#x60;, &#x60;idChecklists&#x60;, &#x60;idLabels&#x60;, &#x60;idList&#x60;, &#x60;idMembers&#x60;, &#x60;idMembersVoted&#x60;, &#x60;idShort&#x60;, &#x60;labels&#x60;, &#x60;manualCoverAttachment&#x60;, &#x60;name&#x60;, &#x60;pos&#x60;, &#x60;shortLink&#x60;, &#x60;shortUrl&#x60;, &#x60;subscribed&#x60;, &#x60;url&#x60; | [optional] [default to all]
 **cards_limit** | **int**| The maximum number of cards to return. Maximum: 1000 | [optional] [default to 10]
 **cards_page** | **float**| The page of results for cards. Maximum: 100 | [optional] [default to 0]
 **card_board** | **bool**| Whether to include the parent board with card results | [optional] [default to false]
 **card_list** | **bool**| Whether to include the parent list with card results | [optional] [default to false]
 **card_members** | **bool**| Whether to include member objects with card results | [optional] [default to false]
 **card_stickers** | **bool**| Whether to include sticker objects with card results | [optional] [default to false]
 **card_attachments** | **str**| Whether to include attachment objects with card results. A boolean value (true or false) or cover for only card cover attachments. | [optional] [default to false]
 **organization_fields** | **str**| all or a comma-separated list of billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url, website | [optional] [default to name,displayName]
 **organizations_limit** | **int**| The maximum number of Workspaces to return. Maximum 1000 | [optional] 
 **member_fields** | **str**| all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url, username | [optional] [default to avatarHash,fullName,initials,username,confirmed]
 **members_limit** | **int**| The maximum number of members to return. Maximum 1000 | [optional] 
 **partial** | **bool**| By default, Trello searches for each word in your query against exactly matching words within Member content. Specifying partial to be true means that we will look for content that starts with any of the words in your query.  If you are looking for a Card titled \&quot;My Development Status Report\&quot;, by default you would need to search for \&quot;Development\&quot;. If you have partial enabled, you will be able to search for \&quot;dev\&quot; but not \&quot;velopment\&quot;. | [optional] [default to false]

### Return type

**list[object]**

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_members**
> list[Member] get_search_members(query, limit=limit, id_board=id_board, id_organization=id_organization, only_org_members=only_org_members)

Search for Members

Search for Trello members.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
query = 'query_example' # str | Search query 1 to 16384 characters long
limit = 8 # int | The maximum number of results to return. Maximum of 20. (optional) (default to 8)
id_board = trello_api_client.TrelloID() # TrelloID |  (optional)
id_organization = trello_api_client.TrelloID() # TrelloID |  (optional)
only_org_members = false # bool |  (optional) (default to false)

try:
    # Search for Members
    api_response = api_instance.get_search_members(query, limit=limit, id_board=id_board, id_organization=id_organization, only_org_members=only_org_members)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_search_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Search query 1 to 16384 characters long | 
 **limit** | **int**| The maximum number of results to return. Maximum of 20. | [optional] [default to 8]
 **id_board** | [**TrelloID**](.md)|  | [optional] 
 **id_organization** | [**TrelloID**](.md)|  | [optional] 
 **only_org_members** | **bool**|  | [optional] [default to false]

### Return type

[**list[Member]**](Member.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokens_token**
> Token get_tokens_token(token, fields=fields, webhooks=webhooks)

Get a Token

Retrieve information about a token.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
token = 'token_example' # str | 
fields = trello_api_client.TokenFields() # TokenFields | `all` or a comma-separated list of `dateCreated`, `dateExpires`, `idMember`, `identifier`, `permissions` (optional)
webhooks = false # bool | Determines whether to include webhooks. (optional) (default to false)

try:
    # Get a Token
    api_response = api_instance.get_tokens_token(token, fields=fields, webhooks=webhooks)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_tokens_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **fields** | [**TokenFields**](.md)| &#x60;all&#x60; or a comma-separated list of &#x60;dateCreated&#x60;, &#x60;dateExpires&#x60;, &#x60;idMember&#x60;, &#x60;identifier&#x60;, &#x60;permissions&#x60; | [optional] 
 **webhooks** | **bool**| Determines whether to include webhooks. | [optional] [default to false]

### Return type

[**Token**](Token.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokens_token_member**
> Member get_tokens_token_member(token, fields=fields)

Get Token's Member

Retrieve information about a token's owner by token.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
token = 'token_example' # str | 
fields = trello_api_client.MemberFields() # MemberFields | `all` or a comma-separated list of valid fields for [Member Object](/cloud/trello/guides/rest-api/object-definitions/). (optional)

try:
    # Get Token's Member
    api_response = api_instance.get_tokens_token_member(token, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_tokens_token_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **fields** | [**MemberFields**](.md)| &#x60;all&#x60; or a comma-separated list of valid fields for [Member Object](/cloud/trello/guides/rest-api/object-definitions/). | [optional] 

### Return type

[**Member**](Member.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokens_token_webhooks**
> list[Webhook] get_tokens_token_webhooks(token)

Get Webhooks for Token

Retrieve all webhooks created with a Token.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
token = 'token_example' # str | 

try:
    # Get Webhooks for Token
    api_response = api_instance.get_tokens_token_webhooks(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_tokens_token_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 

### Return type

[**list[Webhook]**](Webhook.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokens_token_webhooks_idwebhook**
> Webhook get_tokens_token_webhooks_idwebhook(token, id_webhook)

Get a Webhook belonging to a Token

Retrieve a webhook created with a Token.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
token = 'token_example' # str | 
id_webhook = trello_api_client.TrelloID() # TrelloID | ID of the [Webhooks](ref:webhooks) to retrieve.

try:
    # Get a Webhook belonging to a Token
    api_response = api_instance.get_tokens_token_webhooks_idwebhook(token, id_webhook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_tokens_token_webhooks_idwebhook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **id_webhook** | [**TrelloID**](.md)| ID of the [Webhooks](ref:webhooks) to retrieve. | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users_id**
> list[Membership] get_users_id(id, licensed=licensed, deactivated=deactivated, collaborator=collaborator, managed=managed, admin=admin, active_since=active_since, inactive_since=inactive_since, search=search, start_index=start_index)

Get Users of an Enterprise

[BETA] - Get an enterprise's users. You can choose to retrieve licensed members, board guests, etc.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the enterprise to retrieve.
licensed = false # bool | When true, returns members who possess a license for the corresponding Trello Enterprise; when false, returns members who do not. If unspecified, both licensed and unlicensed members will be returned. (optional) (default to false)
deactivated = false # bool | When true, returns members who have been deactivated for the corresponding Trello Enterprise; when false, returns members who have not. If unspecified, both active and deactivated members will be returned. (optional) (default to false)
collaborator = false # bool | When true, returns members who are guests on one or more boards in the corresponding Trello Enterprise (but do not possess a license); when false, returns members who are not. If unspecified, both guests and non-guests will be returned. (optional) (default to false)
managed = false # bool | When true, returns members who are managed by the corresponding Trello Enterprise; when false, returns members who are not. If unspecified, both managed and unmanaged members will be returned. (optional) (default to false)
admin = false # bool | When true, returns members who are administrators of the corresponding Trello Enterprise; when false, returns members who are not. If unspecified, both admin and non-admin members will be returned. (optional) (default to false)
active_since = 'none' # str | Returns only Trello users active since this date (inclusive). (optional) (default to none)
inactive_since = 'none' # str | Returns only Trello users active since this date (inclusive). (optional) (default to none)
search = 'none' # str | Returns members with email address or full name that start with the search value. (optional) (default to none)
start_index = 'none' # str | Cursor to return next set of results (optional) (default to none)

try:
    # Get Users of an Enterprise
    api_response = api_instance.get_users_id(id, licensed=licensed, deactivated=deactivated, collaborator=collaborator, managed=managed, admin=admin, active_since=active_since, inactive_since=inactive_since, search=search, start_index=start_index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_users_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the enterprise to retrieve. | 
 **licensed** | **bool**| When true, returns members who possess a license for the corresponding Trello Enterprise; when false, returns members who do not. If unspecified, both licensed and unlicensed members will be returned. | [optional] [default to false]
 **deactivated** | **bool**| When true, returns members who have been deactivated for the corresponding Trello Enterprise; when false, returns members who have not. If unspecified, both active and deactivated members will be returned. | [optional] [default to false]
 **collaborator** | **bool**| When true, returns members who are guests on one or more boards in the corresponding Trello Enterprise (but do not possess a license); when false, returns members who are not. If unspecified, both guests and non-guests will be returned. | [optional] [default to false]
 **managed** | **bool**| When true, returns members who are managed by the corresponding Trello Enterprise; when false, returns members who are not. If unspecified, both managed and unmanaged members will be returned. | [optional] [default to false]
 **admin** | **bool**| When true, returns members who are administrators of the corresponding Trello Enterprise; when false, returns members who are not. If unspecified, both admin and non-admin members will be returned. | [optional] [default to false]
 **active_since** | **str**| Returns only Trello users active since this date (inclusive). | [optional] [default to none]
 **inactive_since** | **str**| Returns only Trello users active since this date (inclusive). | [optional] [default to none]
 **search** | **str**| Returns members with email address or full name that start with the search value. | [optional] [default to none]
 **start_index** | **str**| Cursor to return next set of results | [optional] [default to none]

### Return type

[**list[Membership]**](Membership.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhooks_id**
> Webhook get_webhooks_id(id)

Get a Webhook

Get a webhook by ID. You must use the token query parameter and pass in the token the webhook was created under, or else you will encounter a 'webhook does not belong to token' error.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the webhook to retrieve.

try:
    # Get a Webhook
    api_response = api_instance.get_webhooks_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_webhooks_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the webhook to retrieve. | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **membersidavatar**
> membersidavatar(id, file)

Create Avatar for Member

Create a new avatar for a member

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
file = 'file_example' # str | 

try:
    # Create Avatar for Member
    api_instance.membersidavatar(id, file)
except ApiException as e:
    print("Exception when calling DefaultApi->membersidavatar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **file** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **membersidcustomboardbackgrounds1**
> BoardBackground membersidcustomboardbackgrounds1(id, file)

Create a new custom Board Background

Upload a new custom board background

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member
file = 'file_example' # str | 

try:
    # Create a new custom Board Background
    api_response = api_instance.membersidcustomboardbackgrounds1(id, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->membersidcustomboardbackgrounds1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 
 **file** | **str**|  | 

### Return type

[**BoardBackground**](BoardBackground.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **membersidcustomemojiidemoji**
> CustomEmoji membersidcustomemojiidemoji(id, id_emoji, fields=fields)

Get a Member's custom Emoji

Get a Member's custom Emoji

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member
id_emoji = trello_api_client.TrelloID() # TrelloID | The ID of the custom emoji
fields = 'all' # str | `all` or a comma-separated list of `name`, `url` (optional) (default to all)

try:
    # Get a Member's custom Emoji
    api_response = api_instance.membersidcustomemojiidemoji(id, id_emoji, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->membersidcustomemojiidemoji: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 
 **id_emoji** | [**TrelloID**](.md)| The ID of the custom emoji | 
 **fields** | **str**| &#x60;all&#x60; or a comma-separated list of &#x60;name&#x60;, &#x60;url&#x60; | [optional] [default to all]

### Return type

[**CustomEmoji**](CustomEmoji.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notificationsidmember**
> InlineResponse2001 notificationsidmember(id, fields=fields)

Get the Member a Notification is about (not the creator)

Get the member (not the creator) a notification is about

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the notification
fields = trello_api_client.MemberFields() # MemberFields | `all` or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/) (optional)

try:
    # Get the Member a Notification is about (not the creator)
    api_response = api_instance.notificationsidmember(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->notificationsidmember: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the notification | 
 **fields** | [**MemberFields**](.md)| &#x60;all&#x60; or a comma-separated list of member [fields](/cloud/trello/guides/rest-api/object-definitions/) | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organizations_id_members_idmember_all**
> organizations_id_members_idmember_all(id, id_member)

Remove a Member from an Organization and all Organization Boards

Remove a member from a Workspace and from all Workspace boards

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or name of the organization
id_member = trello_api_client.TrelloID() # TrelloID | The ID of the member to remove from the Workspace

try:
    # Remove a Member from an Organization and all Organization Boards
    api_instance.organizations_id_members_idmember_all(id, id_member)
except ApiException as e:
    print("Exception when calling DefaultApi->organizations_id_members_idmember_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or name of the organization | 
 **id_member** | [**TrelloID**](.md)| The ID of the member to remove from the Workspace | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_actions_idaction_reactions**
> post_actions_idaction_reactions(id_action, body=body)

Create Reaction for Action

Adds a new reaction to an action

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id_action = trello_api_client.TrelloID() # TrelloID | The ID of the action
body = trello_api_client.IdActionReactionsBody() # IdActionReactionsBody |  (optional)

try:
    # Create Reaction for Action
    api_instance.post_actions_idaction_reactions(id_action, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->post_actions_idaction_reactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_action** | [**TrelloID**](.md)| The ID of the action | 
 **body** | [**IdActionReactionsBody**](IdActionReactionsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_boards**
> post_boards(name, default_labels=default_labels, default_lists=default_lists, desc=desc, id_organization=id_organization, id_board_source=id_board_source, keep_from_source=keep_from_source, power_ups=power_ups, prefs_permission_level=prefs_permission_level, prefs_voting=prefs_voting, prefs_comments=prefs_comments, prefs_invitations=prefs_invitations, prefs_self_join=prefs_self_join, prefs_card_covers=prefs_card_covers, prefs_background=prefs_background, prefs_card_aging=prefs_card_aging)

Create a Board

Create a new board.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
name = 'name_example' # str | The new name for the board. 1 to 16384 characters long.
default_labels = true # bool | Determines whether to use the default set of labels. (optional) (default to true)
default_lists = true # bool | Determines whether to add the default set of lists to a board (To Do, Doing, Done). It is ignored if `idBoardSource` is provided. (optional) (default to true)
desc = 'desc_example' # str | A new description for the board, 0 to 16384 characters long (optional)
id_organization = trello_api_client.TrelloID() # TrelloID | The id or name of the Workspace the board should belong to. (optional)
id_board_source = trello_api_client.TrelloID() # TrelloID | The id of a board to copy into the new board. (optional)
keep_from_source = 'none' # str | To keep cards from the original board pass in the value `cards` (optional) (default to none)
power_ups = 'power_ups_example' # str | The Power-Ups that should be enabled on the new board. One of: `all`, `calendar`, `cardAging`, `recap`, `voting`. (optional)
prefs_permission_level = 'private' # str | The permissions level of the board. One of: `org`, `private`, `public`. (optional) (default to private)
prefs_voting = 'disabled' # str | Who can vote on this board. One of `disabled`, `members`, `observers`, `org`, `public`. (optional) (default to disabled)
prefs_comments = 'members' # str | Who can comment on cards on this board. One of: `disabled`, `members`, `observers`, `org`, `public`. (optional) (default to members)
prefs_invitations = 'members' # str | Determines what types of members can invite users to join. One of: `admins`, `members`. (optional) (default to members)
prefs_self_join = true # bool | Determines whether users can join the boards themselves or whether they have to be invited. (optional) (default to true)
prefs_card_covers = true # bool | Determines whether card covers are enabled. (optional) (default to true)
prefs_background = 'blue' # str | The id of a custom background or one of: `blue`, `orange`, `green`, `red`, `purple`, `pink`, `lime`, `sky`, `grey`. (optional) (default to blue)
prefs_card_aging = 'regular' # str | Determines the type of card aging that should take place on the board if card aging is enabled. One of: `pirate`, `regular`. (optional) (default to regular)

try:
    # Create a Board
    api_instance.post_boards(name, default_labels=default_labels, default_lists=default_lists, desc=desc, id_organization=id_organization, id_board_source=id_board_source, keep_from_source=keep_from_source, power_ups=power_ups, prefs_permission_level=prefs_permission_level, prefs_voting=prefs_voting, prefs_comments=prefs_comments, prefs_invitations=prefs_invitations, prefs_self_join=prefs_self_join, prefs_card_covers=prefs_card_covers, prefs_background=prefs_background, prefs_card_aging=prefs_card_aging)
except ApiException as e:
    print("Exception when calling DefaultApi->post_boards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The new name for the board. 1 to 16384 characters long. | 
 **default_labels** | **bool**| Determines whether to use the default set of labels. | [optional] [default to true]
 **default_lists** | **bool**| Determines whether to add the default set of lists to a board (To Do, Doing, Done). It is ignored if &#x60;idBoardSource&#x60; is provided. | [optional] [default to true]
 **desc** | **str**| A new description for the board, 0 to 16384 characters long | [optional] 
 **id_organization** | [**TrelloID**](.md)| The id or name of the Workspace the board should belong to. | [optional] 
 **id_board_source** | [**TrelloID**](.md)| The id of a board to copy into the new board. | [optional] 
 **keep_from_source** | **str**| To keep cards from the original board pass in the value &#x60;cards&#x60; | [optional] [default to none]
 **power_ups** | **str**| The Power-Ups that should be enabled on the new board. One of: &#x60;all&#x60;, &#x60;calendar&#x60;, &#x60;cardAging&#x60;, &#x60;recap&#x60;, &#x60;voting&#x60;. | [optional] 
 **prefs_permission_level** | **str**| The permissions level of the board. One of: &#x60;org&#x60;, &#x60;private&#x60;, &#x60;public&#x60;. | [optional] [default to private]
 **prefs_voting** | **str**| Who can vote on this board. One of &#x60;disabled&#x60;, &#x60;members&#x60;, &#x60;observers&#x60;, &#x60;org&#x60;, &#x60;public&#x60;. | [optional] [default to disabled]
 **prefs_comments** | **str**| Who can comment on cards on this board. One of: &#x60;disabled&#x60;, &#x60;members&#x60;, &#x60;observers&#x60;, &#x60;org&#x60;, &#x60;public&#x60;. | [optional] [default to members]
 **prefs_invitations** | **str**| Determines what types of members can invite users to join. One of: &#x60;admins&#x60;, &#x60;members&#x60;. | [optional] [default to members]
 **prefs_self_join** | **bool**| Determines whether users can join the boards themselves or whether they have to be invited. | [optional] [default to true]
 **prefs_card_covers** | **bool**| Determines whether card covers are enabled. | [optional] [default to true]
 **prefs_background** | **str**| The id of a custom background or one of: &#x60;blue&#x60;, &#x60;orange&#x60;, &#x60;green&#x60;, &#x60;red&#x60;, &#x60;purple&#x60;, &#x60;pink&#x60;, &#x60;lime&#x60;, &#x60;sky&#x60;, &#x60;grey&#x60;. | [optional] [default to blue]
 **prefs_card_aging** | **str**| Determines the type of card aging that should take place on the board if card aging is enabled. One of: &#x60;pirate&#x60;, &#x60;regular&#x60;. | [optional] [default to regular]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_boards_id_boardplugins**
> post_boards_id_boardplugins(id, id_plugin=id_plugin)

Enable a Power-Up on a Board

Enable a Power-Up on a Board

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Board
id_plugin = trello_api_client.TrelloID() # TrelloID | The ID of the Power-Up to enable (optional)

try:
    # Enable a Power-Up on a Board
    api_instance.post_boards_id_boardplugins(id, id_plugin=id_plugin)
except ApiException as e:
    print("Exception when calling DefaultApi->post_boards_id_boardplugins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Board | 
 **id_plugin** | [**TrelloID**](.md)| The ID of the Power-Up to enable | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_boards_id_calendarkey_generate**
> post_boards_id_calendarkey_generate(id)

Create a calendarKey for a Board

Create a new board.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The id of the board to update

try:
    # Create a calendarKey for a Board
    api_instance.post_boards_id_calendarkey_generate(id)
except ApiException as e:
    print("Exception when calling DefaultApi->post_boards_id_calendarkey_generate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The id of the board to update | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_boards_id_emailkey_generate**
> post_boards_id_emailkey_generate(id)

Create a emailKey for a Board

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The id of the board to update

try:
    # Create a emailKey for a Board
    api_instance.post_boards_id_emailkey_generate(id)
except ApiException as e:
    print("Exception when calling DefaultApi->post_boards_id_emailkey_generate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The id of the board to update | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_boards_id_idtags**
> post_boards_id_idtags(id, value)

Create a Tag for a Board

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The id of the board to update
value = trello_api_client.TrelloID() # TrelloID | The id of a tag from the organization to which this board belongs.

try:
    # Create a Tag for a Board
    api_instance.post_boards_id_idtags(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->post_boards_id_idtags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The id of the board to update | 
 **value** | [**TrelloID**](.md)| The id of a tag from the organization to which this board belongs. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_boards_id_labels**
> post_boards_id_labels(id, name, color)

Create a Label on a Board

Create a new Label on a Board.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the board to update
name = 'name_example' # str | The name of the label to be created. 1 to 16384 characters long.
color = 'color_example' # str | Sets the color of the new label. Valid values are a label color or `null`.

try:
    # Create a Label on a Board
    api_instance.post_boards_id_labels(id, name, color)
except ApiException as e:
    print("Exception when calling DefaultApi->post_boards_id_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the board to update | 
 **name** | **str**| The name of the label to be created. 1 to 16384 characters long. | 
 **color** | **str**| Sets the color of the new label. Valid values are a label color or &#x60;null&#x60;. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_boards_id_lists**
> TrelloList post_boards_id_lists(id, name, pos=pos)

Create a List on a Board

Create a new List on a Board.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the board
name = 'name_example' # str | The name of the list to be created. 1 to 16384 characters long.
pos = 'top' # str | Determines the position of the list. Valid values: `top`, `bottom`, or a positive number. (optional) (default to top)

try:
    # Create a List on a Board
    api_response = api_instance.post_boards_id_lists(id, name, pos=pos)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_boards_id_lists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the board | 
 **name** | **str**| The name of the list to be created. 1 to 16384 characters long. | 
 **pos** | **str**| Determines the position of the list. Valid values: &#x60;top&#x60;, &#x60;bottom&#x60;, or a positive number. | [optional] [default to top]

### Return type

[**TrelloList**](TrelloList.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_boards_id_markedasviewed**
> post_boards_id_markedasviewed(id)

Mark Board as viewed

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The id of the board to update

try:
    # Mark Board as viewed
    api_instance.post_boards_id_markedasviewed(id)
except ApiException as e:
    print("Exception when calling DefaultApi->post_boards_id_markedasviewed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The id of the board to update | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cards**
> Card post_cards(id_list, name=name, desc=desc, pos=pos, due=due, start=start, due_complete=due_complete, id_members=id_members, id_labels=id_labels, url_source=url_source, file_source=file_source, mime_type=mime_type, id_card_source=id_card_source, keep_from_source=keep_from_source, address=address, location_name=location_name, coordinates=coordinates)

Create a new Card

Create a new card

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id_list = trello_api_client.TrelloID() # TrelloID | The ID of the list the card should be created in
name = 'name_example' # str | The name for the card (optional)
desc = 'desc_example' # str | The description for the card (optional)
pos = trello_api_client.Pos() # Pos | The position of the new card. `top`, `bottom`, or a positive float (optional)
due = '2013-10-20' # date | A due date for the card (optional)
start = '2013-10-20' # date | The start date of a card, or `null` (optional)
due_complete = true # bool |  (optional)
id_members = NULL # list[object] | Comma-separated list of member IDs to add to the card (optional)
id_labels = NULL # list[object] | Comma-separated list of label IDs to add to the card (optional)
url_source = 'url_source_example' # str | A URL starting with `http://` or `https://` (optional)
file_source = 'file_source_example' # str |  (optional)
mime_type = 'mime_type_example' # str | The mimeType of the attachment. Max length 256 (optional)
id_card_source = trello_api_client.TrelloID() # TrelloID | The ID of a card to copy into the new card (optional)
keep_from_source = 'all' # str | If using `idCardSource` you can specify which properties to copy over. `all` or comma-separated list of: `attachments,checklists,customFields,comments,due,start,labels,members,start,stickers` (optional) (default to all)
address = 'address_example' # str | For use with/by the Map View (optional)
location_name = 'location_name_example' # str | For use with/by the Map View (optional)
coordinates = 'coordinates_example' # str | For use with/by the Map View. Should take the form latitude,longitude (optional)

try:
    # Create a new Card
    api_response = api_instance.post_cards(id_list, name=name, desc=desc, pos=pos, due=due, start=start, due_complete=due_complete, id_members=id_members, id_labels=id_labels, url_source=url_source, file_source=file_source, mime_type=mime_type, id_card_source=id_card_source, keep_from_source=keep_from_source, address=address, location_name=location_name, coordinates=coordinates)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_cards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_list** | [**TrelloID**](.md)| The ID of the list the card should be created in | 
 **name** | **str**| The name for the card | [optional] 
 **desc** | **str**| The description for the card | [optional] 
 **pos** | [**Pos**](.md)| The position of the new card. &#x60;top&#x60;, &#x60;bottom&#x60;, or a positive float | [optional] 
 **due** | **date**| A due date for the card | [optional] 
 **start** | **date**| The start date of a card, or &#x60;null&#x60; | [optional] 
 **due_complete** | **bool**|  | [optional] 
 **id_members** | [**list[object]**](object.md)| Comma-separated list of member IDs to add to the card | [optional] 
 **id_labels** | [**list[object]**](object.md)| Comma-separated list of label IDs to add to the card | [optional] 
 **url_source** | **str**| A URL starting with &#x60;http://&#x60; or &#x60;https://&#x60; | [optional] 
 **file_source** | **str**|  | [optional] 
 **mime_type** | **str**| The mimeType of the attachment. Max length 256 | [optional] 
 **id_card_source** | [**TrelloID**](.md)| The ID of a card to copy into the new card | [optional] 
 **keep_from_source** | **str**| If using &#x60;idCardSource&#x60; you can specify which properties to copy over. &#x60;all&#x60; or comma-separated list of: &#x60;attachments,checklists,customFields,comments,due,start,labels,members,start,stickers&#x60; | [optional] [default to all]
 **address** | **str**| For use with/by the Map View | [optional] 
 **location_name** | **str**| For use with/by the Map View | [optional] 
 **coordinates** | **str**| For use with/by the Map View. Should take the form latitude,longitude | [optional] 

### Return type

[**Card**](Card.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cards_id_actions_comments**
> Action post_cards_id_actions_comments(id, text)

Add a new comment to a Card

Add a new comment to a card

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
text = 'text_example' # str | The comment

try:
    # Add a new comment to a Card
    api_response = api_instance.post_cards_id_actions_comments(id, text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_cards_id_actions_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **text** | **str**| The comment | 

### Return type

[**Action**](Action.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cards_id_attachments**
> list[object] post_cards_id_attachments(id, name=name, file=file, mime_type=mime_type, url=url, set_cover=set_cover)

Create Attachment On Card

Create an Attachment to a Card

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
name = 'name_example' # str | The name of the attachment. Max length 256. (optional)
file = 'file_example' # str | The file to attach, as multipart/form-data (optional)
mime_type = 'mime_type_example' # str | The mimeType of the attachment. Max length 256 (optional)
url = 'url_example' # str | A URL to attach. Must start with `http://` or `https://` (optional)
set_cover = false # bool | Determines whether to use the new attachment as a cover for the Card. (optional) (default to false)

try:
    # Create Attachment On Card
    api_response = api_instance.post_cards_id_attachments(id, name=name, file=file, mime_type=mime_type, url=url, set_cover=set_cover)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_cards_id_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **name** | **str**| The name of the attachment. Max length 256. | [optional] 
 **file** | **str**| The file to attach, as multipart/form-data | [optional] 
 **mime_type** | **str**| The mimeType of the attachment. Max length 256 | [optional] 
 **url** | **str**| A URL to attach. Must start with &#x60;http://&#x60; or &#x60;https://&#x60; | [optional] 
 **set_cover** | **bool**| Determines whether to use the new attachment as a cover for the Card. | [optional] [default to false]

### Return type

**list[object]**

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cards_id_checklists**
> post_cards_id_checklists(id, name=name, id_checklist_source=id_checklist_source, pos=pos)

Create Checklist on a Card

Create a new checklist on a card

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
name = 'name_example' # str | The name of the checklist (optional)
id_checklist_source = trello_api_client.TrelloID() # TrelloID | The ID of a source checklist to copy into the new one (optional)
pos = 'pos_example' # str | The position of the checklist on the card. One of: `top`, `bottom`, or a positive number. (optional)

try:
    # Create Checklist on a Card
    api_instance.post_cards_id_checklists(id, name=name, id_checklist_source=id_checklist_source, pos=pos)
except ApiException as e:
    print("Exception when calling DefaultApi->post_cards_id_checklists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **name** | **str**| The name of the checklist | [optional] 
 **id_checklist_source** | [**TrelloID**](.md)| The ID of a source checklist to copy into the new one | [optional] 
 **pos** | **str**| The position of the checklist on the card. One of: &#x60;top&#x60;, &#x60;bottom&#x60;, or a positive number. | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cards_id_idlabels**
> post_cards_id_idlabels(id, value=value)

Add a Label to a Card

Add a label to a card

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
value = trello_api_client.TrelloID() # TrelloID | The ID of the label to add (optional)

try:
    # Add a Label to a Card
    api_instance.post_cards_id_idlabels(id, value=value)
except ApiException as e:
    print("Exception when calling DefaultApi->post_cards_id_idlabels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **value** | [**TrelloID**](.md)| The ID of the label to add | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cards_id_idmembers**
> post_cards_id_idmembers(id, value=value)

Add a Member to a Card

Add a member to a card

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
value = trello_api_client.TrelloID() # TrelloID | The ID of the Member to add to the card (optional)

try:
    # Add a Member to a Card
    api_instance.post_cards_id_idmembers(id, value=value)
except ApiException as e:
    print("Exception when calling DefaultApi->post_cards_id_idmembers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **value** | [**TrelloID**](.md)| The ID of the Member to add to the card | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cards_id_labels**
> post_cards_id_labels(id, color, name=name)

Create a new Label on a Card

Create a new label for the board and add it to the given card.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
color = 'color_example' # str | A valid label color or `null`. See [labels](/cloud/trello/guides/rest-api/object-definitions/)
name = 'name_example' # str | A name for the label (optional)

try:
    # Create a new Label on a Card
    api_instance.post_cards_id_labels(id, color, name=name)
except ApiException as e:
    print("Exception when calling DefaultApi->post_cards_id_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **color** | **str**| A valid label color or &#x60;null&#x60;. See [labels](/cloud/trello/guides/rest-api/object-definitions/) | 
 **name** | **str**| A name for the label | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cards_id_markassociatednotificationsread**
> post_cards_id_markassociatednotificationsread(id)

Mark a Card's Notifications as read

Mark notifications about this card as read

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card

try:
    # Mark a Card's Notifications as read
    api_instance.post_cards_id_markassociatednotificationsread(id)
except ApiException as e:
    print("Exception when calling DefaultApi->post_cards_id_markassociatednotificationsread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cards_id_stickers**
> post_cards_id_stickers(id, image, top, left, z_index, rotate=rotate)

Add a Sticker to a Card

Add a sticker to a card

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
image = 'image_example' # str | For custom stickers, the id of the sticker. For default stickers, the string identifier (like 'taco-cool', see below)
top = 3.4 # float | The top position of the sticker, from -60 to 100
left = 3.4 # float | The left position of the sticker, from -60 to 100
z_index = 56 # int | The z-index of the sticker
rotate = 0 # float | The rotation of the sticker (optional) (default to 0)

try:
    # Add a Sticker to a Card
    api_instance.post_cards_id_stickers(id, image, top, left, z_index, rotate=rotate)
except ApiException as e:
    print("Exception when calling DefaultApi->post_cards_id_stickers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **image** | **str**| For custom stickers, the id of the sticker. For default stickers, the string identifier (like &#x27;taco-cool&#x27;, see below) | 
 **top** | **float**| The top position of the sticker, from -60 to 100 | 
 **left** | **float**| The left position of the sticker, from -60 to 100 | 
 **z_index** | **int**| The z-index of the sticker | 
 **rotate** | **float**| The rotation of the sticker | [optional] [default to 0]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_checklists**
> post_checklists(id_card, name=name, pos=pos, id_checklist_source=id_checklist_source)

Create a Checklist

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id_card = trello_api_client.TrelloID() # TrelloID | The ID of the Card that the checklist should be added to.
name = 'name_example' # str | The name of the checklist. Should be a string of length 1 to 16384. (optional)
pos = trello_api_client.PosStringOrNumber() # PosStringOrNumber | The position of the checklist on the card. One of: `top`, `bottom`, or a positive number. (optional)
id_checklist_source = trello_api_client.TrelloID() # TrelloID | The ID of a checklist to copy into the new checklist. (optional)

try:
    # Create a Checklist
    api_instance.post_checklists(id_card, name=name, pos=pos, id_checklist_source=id_checklist_source)
except ApiException as e:
    print("Exception when calling DefaultApi->post_checklists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_card** | [**TrelloID**](.md)| The ID of the Card that the checklist should be added to. | 
 **name** | **str**| The name of the checklist. Should be a string of length 1 to 16384. | [optional] 
 **pos** | [**PosStringOrNumber**](.md)| The position of the checklist on the card. One of: &#x60;top&#x60;, &#x60;bottom&#x60;, or a positive number. | [optional] 
 **id_checklist_source** | [**TrelloID**](.md)| The ID of a checklist to copy into the new checklist. | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_checklists_id_checkitems**
> post_checklists_id_checkitems(id, name, pos=pos, checked=checked, due=due, due_reminder=due_reminder, id_member=id_member)

Create Checkitem on Checklist

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of a checklist.
name = 'name_example' # str | The name of the new check item on the checklist. Should be a string of length 1 to 16384.
pos = trello_api_client.PosStringOrNumber() # PosStringOrNumber | The position of the check item in the checklist. One of: `top`, `bottom`, or a positive number. (optional)
checked = false # bool | Determines whether the check item is already checked when created. (optional) (default to false)
due = '2013-10-20' # date | A due date for the checkitem (optional)
due_reminder = 1.2 # float | A dueReminder for the due date on the checkitem (optional)
id_member = trello_api_client.TrelloID() # TrelloID | An ID of a member resource. (optional)

try:
    # Create Checkitem on Checklist
    api_instance.post_checklists_id_checkitems(id, name, pos=pos, checked=checked, due=due, due_reminder=due_reminder, id_member=id_member)
except ApiException as e:
    print("Exception when calling DefaultApi->post_checklists_id_checkitems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of a checklist. | 
 **name** | **str**| The name of the new check item on the checklist. Should be a string of length 1 to 16384. | 
 **pos** | **PosStringOrNumber**| The position of the check item in the checklist. One of: &#x60;top&#x60;, &#x60;bottom&#x60;, or a positive number. | [optional] 
 **checked** | **bool**| Determines whether the check item is already checked when created. | [optional] [default to false]
 **due** | **date**| A due date for the checkitem | [optional] 
 **due_reminder** | **float**| A dueReminder for the due date on the checkitem | [optional] 
 **id_member** | [**TrelloID**](.md)| An ID of a member resource. | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_customfields**
> CustomField post_customfields(body=body)

Create a new Custom Field on a Board

Create a new Custom Field on a board.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
body = trello_api_client.CustomFieldsBody() # CustomFieldsBody |  (optional)

try:
    # Create a new Custom Field on a Board
    api_response = api_instance.post_customfields(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_customfields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomFieldsBody**](CustomFieldsBody.md)|  | [optional] 

### Return type

[**CustomField**](CustomField.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_customfields_id_options**
> post_customfields_id_options(id)

Get Options of Custom Field drop down

Get the options of a drop down Custom Field

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the customfield.

try:
    # Get Options of Custom Field drop down
    api_instance.post_customfields_id_options(id)
except ApiException as e:
    print("Exception when calling DefaultApi->post_customfields_id_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the customfield. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_enterprises_id_tokens**
> post_enterprises_id_tokens(id, expiration=expiration)

Create an auth Token for an Enterprise.

Create an auth Token for an Enterprise.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = 'id_example' # str | ID of the enterprise to retrieve.
expiration = 'none' # str | One of: `1hour`, `1day`, `30days`, `never` (optional) (default to none)

try:
    # Create an auth Token for an Enterprise.
    api_instance.post_enterprises_id_tokens(id, expiration=expiration)
except ApiException as e:
    print("Exception when calling DefaultApi->post_enterprises_id_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the enterprise to retrieve. | 
 **expiration** | **str**| One of: &#x60;1hour&#x60;, &#x60;1day&#x60;, &#x60;30days&#x60;, &#x60;never&#x60; | [optional] [default to none]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_labels**
> post_labels(name, color, id_board)

Create a Label

Create a new Label on a Board.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
name = 'name_example' # str | Name for the label
color = trello_api_client.Color() # Color | The color for the label.
id_board = 'id_board_example' # str | The ID of the Board to create the Label on.

try:
    # Create a Label
    api_instance.post_labels(name, color, id_board)
except ApiException as e:
    print("Exception when calling DefaultApi->post_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name for the label | 
 **color** | [**Color**](.md)| The color for the label. | 
 **id_board** | **str**| The ID of the Board to create the Label on. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_lists**
> post_lists(name, id_board, id_list_source=id_list_source, pos=pos)

Create a new List

Create a new List on a Board

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
name = 'name_example' # str | Name for the list
id_board = trello_api_client.TrelloID() # TrelloID | The long ID of the board the list should be created on
id_list_source = trello_api_client.TrelloID() # TrelloID | ID of the List to copy into the new List (optional)
pos = trello_api_client.Pos3() # Pos3 | Position of the list. `top`, `bottom`, or a positive floating point number (optional)

try:
    # Create a new List
    api_instance.post_lists(name, id_board, id_list_source=id_list_source, pos=pos)
except ApiException as e:
    print("Exception when calling DefaultApi->post_lists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name for the list | 
 **id_board** | [**TrelloID**](.md)| The long ID of the board the list should be created on | 
 **id_list_source** | [**TrelloID**](.md)| ID of the List to copy into the new List | [optional] 
 **pos** | [**Pos3**](.md)| Position of the list. &#x60;top&#x60;, &#x60;bottom&#x60;, or a positive floating point number | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_lists_id_archiveallcards**
> post_lists_id_archiveallcards(id)

Archive all Cards in List

Archive all cards in a list

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the list

try:
    # Archive all Cards in List
    api_instance.post_lists_id_archiveallcards(id)
except ApiException as e:
    print("Exception when calling DefaultApi->post_lists_id_archiveallcards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the list | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_lists_id_moveallcards**
> post_lists_id_moveallcards(id, id_board, id_list)

Move all Cards in List

Move all Cards in a List

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the list
id_board = trello_api_client.TrelloID() # TrelloID | The ID of the board the cards should be moved to
id_list = trello_api_client.TrelloID() # TrelloID | The ID of the list that the cards should be moved to

try:
    # Move all Cards in List
    api_instance.post_lists_id_moveallcards(id, id_board, id_list)
except ApiException as e:
    print("Exception when calling DefaultApi->post_lists_id_moveallcards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the list | 
 **id_board** | [**TrelloID**](.md)| The ID of the board the cards should be moved to | 
 **id_list** | [**TrelloID**](.md)| The ID of the list that the cards should be moved to | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_members_id_boardbackgrounds1**
> list[object] post_members_id_boardbackgrounds1(id, file)

Upload new boardBackground for Member

Upload a new boardBackground

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member
file = 'file_example' # str | 

try:
    # Upload new boardBackground for Member
    api_response = api_instance.post_members_id_boardbackgrounds1(id, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_members_id_boardbackgrounds1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 
 **file** | **str**|  | 

### Return type

**list[object]**

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_members_id_boardstars**
> list[BoardStars] post_members_id_boardstars(id, id_board, pos)

Create Star for Board

Star a new board on behalf of a Member

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.Id1() # Id1 | The ID or username of the member
id_board = trello_api_client.TrelloID() # TrelloID | The ID of the board to star
pos = trello_api_client.PosStringOrNumber() # PosStringOrNumber | The position of the newly starred board. `top`, `bottom`, or a positive float.

try:
    # Create Star for Board
    api_response = api_instance.post_members_id_boardstars(id, id_board, pos)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_members_id_boardstars: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id1**](.md)| The ID or username of the member | 
 **id_board** | [**TrelloID**](.md)| The ID of the board to star | 
 **pos** | [**PosStringOrNumber**](.md)| The position of the newly starred board. &#x60;top&#x60;, &#x60;bottom&#x60;, or a positive float. | 

### Return type

[**list[BoardStars]**](BoardStars.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_members_id_customemoji**
> CustomEmoji post_members_id_customemoji(id, file, name)

Create custom Emoji for Member

Create a new custom Emoji

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member
file = 'file_example' # str | 
name = 'name_example' # str | Name for the emoji. 2 - 64 characters

try:
    # Create custom Emoji for Member
    api_response = api_instance.post_members_id_customemoji(id, file, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_members_id_customemoji: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 
 **file** | **str**|  | 
 **name** | **str**| Name for the emoji. 2 - 64 characters | 

### Return type

[**CustomEmoji**](CustomEmoji.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_members_id_customstickers**
> CustomSticker post_members_id_customstickers(id, file)

Create custom Sticker for Member

Upload a new custom sticker

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member
file = 'file_example' # str | 

try:
    # Create custom Sticker for Member
    api_response = api_instance.post_members_id_customstickers(id, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_members_id_customstickers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 
 **file** | **str**|  | 

### Return type

[**CustomSticker**](CustomSticker.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_members_id_onetimemessagesdismissed**
> post_members_id_onetimemessagesdismissed(id, value)

Dismiss a message for Member

Dismiss a message

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member
value = trello_api_client.TrelloID() # TrelloID | The message to dismiss

try:
    # Dismiss a message for Member
    api_instance.post_members_id_onetimemessagesdismissed(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->post_members_id_onetimemessagesdismissed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 
 **value** | [**TrelloID**](.md)| The message to dismiss | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_members_id_savedsearches**
> SavedSearch post_members_id_savedsearches(id, name, query, pos)

Create saved Search for Member

Create a saved search

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member
name = 'name_example' # str | The name for the saved search
query = 'query_example' # str | The search query
pos = trello_api_client.PosStringOrNumber() # PosStringOrNumber | The position of the saved search. `top`, `bottom`, or a positive float.

try:
    # Create saved Search for Member
    api_response = api_instance.post_members_id_savedsearches(id, name, query, pos)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_members_id_savedsearches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 
 **name** | **str**| The name for the saved search | 
 **query** | **str**| The search query | 
 **pos** | [**PosStringOrNumber**](.md)| The position of the saved search. &#x60;top&#x60;, &#x60;bottom&#x60;, or a positive float. | 

### Return type

[**SavedSearch**](SavedSearch.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_notifications_all_read**
> InlineResponse2002 post_notifications_all_read(read=read, ids=ids)

Mark all Notifications as read

Mark all notifications as read

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
read = true # bool | Boolean to specify whether to mark as read or unread (defaults to `true`, marking as read) (optional) (default to true)
ids = [trello_api_client.TrelloID()] # list[TrelloID] | A comma-seperated list of IDs. Allows specifying an array of notification IDs to change the read state for. This will become useful as we add grouping of notifications to the UI, with a single button to mark all notifications in the group as read/unread. (optional)

try:
    # Mark all Notifications as read
    api_response = api_instance.post_notifications_all_read(read=read, ids=ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_notifications_all_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **read** | **bool**| Boolean to specify whether to mark as read or unread (defaults to &#x60;true&#x60;, marking as read) | [optional] [default to true]
 **ids** | [**list[TrelloID]**](TrelloID.md)| A comma-seperated list of IDs. Allows specifying an array of notification IDs to change the read state for. This will become useful as we add grouping of notifications to the UI, with a single button to mark all notifications in the group as read/unread. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_organizations**
> InlineResponse2006 post_organizations(display_name, desc=desc, name=name, website=website)

Create a new Organization

Create a new Workspace

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
display_name = 'display_name_example' # str | The name to display for the Organization
desc = 'desc_example' # str | The description for the organizations (optional)
name = 'name_example' # str | A string with a length of at least 3. Only lowercase letters, underscores, and numbers are allowed. If the name contains invalid characters, they will be removed. If the name conflicts with an existing name, a new name will be substituted. (optional)
website = 'website_example' # str | A URL starting with `http://` or `https://` (optional)

try:
    # Create a new Organization
    api_response = api_instance.post_organizations(display_name, desc=desc, name=name, website=website)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_organizations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_name** | **str**| The name to display for the Organization | 
 **desc** | **str**| The description for the organizations | [optional] 
 **name** | **str**| A string with a length of at least 3. Only lowercase letters, underscores, and numbers are allowed. If the name contains invalid characters, they will be removed. If the name conflicts with an existing name, a new name will be substituted. | [optional] 
 **website** | **str**| A URL starting with &#x60;http://&#x60; or &#x60;https://&#x60; | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_organizations_id_exports**
> Export post_organizations_id_exports(id, attachments=attachments)

Create Export for Organizations

Kick off CSV export for an organization

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or name of the Workspace
attachments = true # bool | Whether the CSV should include attachments or not. (optional) (default to true)

try:
    # Create Export for Organizations
    api_response = api_instance.post_organizations_id_exports(id, attachments=attachments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_organizations_id_exports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or name of the Workspace | 
 **attachments** | **bool**| Whether the CSV should include attachments or not. | [optional] [default to true]

### Return type

[**Export**](Export.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_organizations_id_logo**
> InlineResponse2006 post_organizations_id_logo(id, file=file)

Update logo for an Organization

Set the logo image for a Workspace

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or name of the Workspace
file = 'file_example' # str | Image file for the logo (optional)

try:
    # Update logo for an Organization
    api_response = api_instance.post_organizations_id_logo(id, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_organizations_id_logo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or name of the Workspace | 
 **file** | **str**| Image file for the logo | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_organizations_id_tags**
> InlineResponse2008 post_organizations_id_tags(id)

Create a Tag in Organization

Create a Tag in an Organization

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.Id6() # Id6 | The ID or name of the Organization

try:
    # Create a Tag in Organization
    api_response = api_instance.post_organizations_id_tags(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_organizations_id_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id6**](.md)| The ID or name of the Organization | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_plugins_idplugin_listing**
> PluginListing post_plugins_idplugin_listing(id_plugin, body=body)

Create a Listing for Plugin

Create a new listing for a given locale for your Power-Up

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id_plugin = trello_api_client.TrelloID() # TrelloID | The ID of the Power-Up for which you are creating a new listing.
body = trello_api_client.IdPluginListingBody() # IdPluginListingBody |  (optional)

try:
    # Create a Listing for Plugin
    api_response = api_instance.post_plugins_idplugin_listing(id_plugin, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_plugins_idplugin_listing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_plugin** | [**TrelloID**](.md)| The ID of the Power-Up for which you are creating a new listing. | 
 **body** | [**IdPluginListingBody**](IdPluginListingBody.md)|  | [optional] 

### Return type

[**PluginListing**](PluginListing.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tokens_token_webhooks**
> Webhook post_tokens_token_webhooks(token, callback_url, id_model, description=description)

Create Webhooks for Token

Create a new webhook for a Token.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
token = 'token_example' # str | 
callback_url = 'callback_url_example' # str | The URL that the webhook should POST information to.
id_model = trello_api_client.TrelloID() # TrelloID | ID of the object to create a webhook on.
description = 'description_example' # str | A description to be displayed when retrieving information about the webhook. (optional)

try:
    # Create Webhooks for Token
    api_response = api_instance.post_tokens_token_webhooks(token, callback_url, id_model, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_tokens_token_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **callback_url** | **str**| The URL that the webhook should POST information to. | 
 **id_model** | [**TrelloID**](.md)| ID of the object to create a webhook on. | 
 **description** | **str**| A description to be displayed when retrieving information about the webhook. | [optional] 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_webhooks**
> Webhook post_webhooks(callback_url, id_model, description=description, active=active)

Create a Webhook

Create a new webhook.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
callback_url = 'callback_url_example' # str | A valid URL that is reachable with a `HEAD` and `POST` request.
id_model = trello_api_client.TrelloID() # TrelloID | ID of the model to be monitored
description = 'description_example' # str | A string with a length from `0` to `16384`. (optional)
active = true # bool | Determines whether the webhook is active and sending `POST` requests. (optional)

try:
    # Create a Webhook
    api_response = api_instance.post_webhooks(callback_url, id_model, description=description, active=active)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->post_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **callback_url** | **str**| A valid URL that is reachable with a &#x60;HEAD&#x60; and &#x60;POST&#x60; request. | 
 **id_model** | [**TrelloID**](.md)| ID of the model to be monitored | 
 **description** | **str**| A string with a length from &#x60;0&#x60; to &#x60;16384&#x60;. | [optional] 
 **active** | **bool**| Determines whether the webhook is active and sending &#x60;POST&#x60; requests. | [optional] 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_actions_id**
> put_actions_id(id, text)

Update an Action

Update a specific Action. Only comment actions can be updated. Used to edit the content of a comment.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Action
text = 'text_example' # str | The new text for the comment

try:
    # Update an Action
    api_instance.put_actions_id(id, text)
except ApiException as e:
    print("Exception when calling DefaultApi->put_actions_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Action | 
 **text** | **str**| The new text for the comment | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_actions_id_text**
> put_actions_id_text(id, value)

Update a Comment Action

Update a comment action

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the action to update
value = 'value_example' # str | The new text for the comment

try:
    # Update a Comment Action
    api_instance.put_actions_id_text(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->put_actions_id_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the action to update | 
 **value** | **str**| The new text for the comment | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_boards_id**
> put_boards_id(id, name=name, desc=desc, closed=closed, subscribed=subscribed, id_organization=id_organization, prefspermission_level=prefspermission_level, prefsself_join=prefsself_join, prefscard_covers=prefscard_covers, prefshide_votes=prefshide_votes, prefsinvitations=prefsinvitations, prefsvoting=prefsvoting, prefscomments=prefscomments, prefsbackground=prefsbackground, prefscard_aging=prefscard_aging, prefscalendar_feed_enabled=prefscalendar_feed_enabled, label_namesgreen=label_namesgreen, label_namesyellow=label_namesyellow, label_namesorange=label_namesorange, label_namesred=label_namesred, label_namespurple=label_namespurple, label_namesblue=label_namesblue)

Update a Board

Update an existing board by id

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | 
name = 'name_example' # str | The new name for the board. 1 to 16384 characters long. (optional)
desc = 'desc_example' # str | A new description for the board, 0 to 16384 characters long (optional)
closed = true # bool | Whether the board is closed (optional)
subscribed = trello_api_client.TrelloID() # TrelloID | Whether the acting user is subscribed to the board (optional)
id_organization = 'id_organization_example' # str | The id of the Workspace the board should be moved to (optional)
prefspermission_level = 'prefspermission_level_example' # str | One of: org, private, public (optional)
prefsself_join = true # bool | Whether Workspace members can join the board themselves (optional)
prefscard_covers = true # bool | Whether card covers should be displayed on this board (optional)
prefshide_votes = true # bool | Determines whether the Voting Power-Up should hide who voted on cards or not. (optional)
prefsinvitations = 'prefsinvitations_example' # str | Who can invite people to this board. One of: admins, members (optional)
prefsvoting = 'prefsvoting_example' # str | Who can vote on this board. One of disabled, members, observers, org, public (optional)
prefscomments = 'prefscomments_example' # str | Who can comment on cards on this board. One of: disabled, members, observers, org, public (optional)
prefsbackground = 'prefsbackground_example' # str | The id of a custom background or one of: blue, orange, green, red, purple, pink, lime, sky, grey (optional)
prefscard_aging = 'prefscard_aging_example' # str | One of: pirate, regular (optional)
prefscalendar_feed_enabled = true # bool | Determines whether the calendar feed is enabled or not. (optional)
label_namesgreen = 'label_namesgreen_example' # str | Name for the green label. 1 to 16384 characters long (optional)
label_namesyellow = 'label_namesyellow_example' # str | Name for the yellow label. 1 to 16384 characters long (optional)
label_namesorange = 'label_namesorange_example' # str | Name for the orange label. 1 to 16384 characters long (optional)
label_namesred = 'label_namesred_example' # str | Name for the red label. 1 to 16384 characters long (optional)
label_namespurple = 'label_namespurple_example' # str | Name for the purple label. 1 to 16384 characters long (optional)
label_namesblue = 'label_namesblue_example' # str | Name for the blue label. 1 to 16384 characters long (optional)

try:
    # Update a Board
    api_instance.put_boards_id(id, name=name, desc=desc, closed=closed, subscribed=subscribed, id_organization=id_organization, prefspermission_level=prefspermission_level, prefsself_join=prefsself_join, prefscard_covers=prefscard_covers, prefshide_votes=prefshide_votes, prefsinvitations=prefsinvitations, prefsvoting=prefsvoting, prefscomments=prefscomments, prefsbackground=prefsbackground, prefscard_aging=prefscard_aging, prefscalendar_feed_enabled=prefscalendar_feed_enabled, label_namesgreen=label_namesgreen, label_namesyellow=label_namesyellow, label_namesorange=label_namesorange, label_namesred=label_namesred, label_namespurple=label_namespurple, label_namesblue=label_namesblue)
except ApiException as e:
    print("Exception when calling DefaultApi->put_boards_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)|  | 
 **name** | **str**| The new name for the board. 1 to 16384 characters long. | [optional] 
 **desc** | **str**| A new description for the board, 0 to 16384 characters long | [optional] 
 **closed** | **bool**| Whether the board is closed | [optional] 
 **subscribed** | [**TrelloID**](.md)| Whether the acting user is subscribed to the board | [optional] 
 **id_organization** | **str**| The id of the Workspace the board should be moved to | [optional] 
 **prefspermission_level** | **str**| One of: org, private, public | [optional] 
 **prefsself_join** | **bool**| Whether Workspace members can join the board themselves | [optional] 
 **prefscard_covers** | **bool**| Whether card covers should be displayed on this board | [optional] 
 **prefshide_votes** | **bool**| Determines whether the Voting Power-Up should hide who voted on cards or not. | [optional] 
 **prefsinvitations** | **str**| Who can invite people to this board. One of: admins, members | [optional] 
 **prefsvoting** | **str**| Who can vote on this board. One of disabled, members, observers, org, public | [optional] 
 **prefscomments** | **str**| Who can comment on cards on this board. One of: disabled, members, observers, org, public | [optional] 
 **prefsbackground** | **str**| The id of a custom background or one of: blue, orange, green, red, purple, pink, lime, sky, grey | [optional] 
 **prefscard_aging** | **str**| One of: pirate, regular | [optional] 
 **prefscalendar_feed_enabled** | **bool**| Determines whether the calendar feed is enabled or not. | [optional] 
 **label_namesgreen** | **str**| Name for the green label. 1 to 16384 characters long | [optional] 
 **label_namesyellow** | **str**| Name for the yellow label. 1 to 16384 characters long | [optional] 
 **label_namesorange** | **str**| Name for the orange label. 1 to 16384 characters long | [optional] 
 **label_namesred** | **str**| Name for the red label. 1 to 16384 characters long | [optional] 
 **label_namespurple** | **str**| Name for the purple label. 1 to 16384 characters long | [optional] 
 **label_namesblue** | **str**| Name for the blue label. 1 to 16384 characters long | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_boards_id_members**
> put_boards_id_members(email, id, body=body, type=type)

Invite Member to Board via email

Invite a Member to a Board via their email address.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
email = 'email_example' # str | The email address of a user to add as a member of the board.
id = trello_api_client.TrelloID() # TrelloID | The ID of the board
body = trello_api_client.IdMembersBody() # IdMembersBody |  (optional)
type = 'normal' # str | Valid values: admin, normal, observer. Determines what type of member the user being added should be of the board. (optional) (default to normal)

try:
    # Invite Member to Board via email
    api_instance.put_boards_id_members(email, id, body=body, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->put_boards_id_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The email address of a user to add as a member of the board. | 
 **id** | [**TrelloID**](.md)| The ID of the board | 
 **body** | [**IdMembersBody**](IdMembersBody.md)|  | [optional] 
 **type** | **str**| Valid values: admin, normal, observer. Determines what type of member the user being added should be of the board. | [optional] [default to normal]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_boards_id_members_idmember**
> put_boards_id_members_idmember(id, id_member, type, allow_billable_guest=allow_billable_guest)

Add a Member to a Board

Add a member to the board.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The id of the board to update
id_member = trello_api_client.TrelloID() # TrelloID | The id of the member to add to the board.
type = 'type_example' # str | One of: admin, normal, observer. Determines the type of member this user will be on the board.
allow_billable_guest = false # bool | Optional param that allows organization admins to add multi-board guests onto a board. (optional) (default to false)

try:
    # Add a Member to a Board
    api_instance.put_boards_id_members_idmember(id, id_member, type, allow_billable_guest=allow_billable_guest)
except ApiException as e:
    print("Exception when calling DefaultApi->put_boards_id_members_idmember: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The id of the board to update | 
 **id_member** | [**TrelloID**](.md)| The id of the member to add to the board. | 
 **type** | **str**| One of: admin, normal, observer. Determines the type of member this user will be on the board. | 
 **allow_billable_guest** | **bool**| Optional param that allows organization admins to add multi-board guests onto a board. | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_boards_id_memberships_idmembership**
> put_boards_id_memberships_idmembership(id, id_membership, type, member_fields=member_fields)

Update Membership of Member on a Board

Update an existing board by id

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The id of the board to update
id_membership = trello_api_client.TrelloID() # TrelloID | The id of a membership that should be added to this board.
type = 'type_example' # str | One of: admin, normal, observer. Determines the type of member that this membership will be to this board.
member_fields = 'fullName, username' # str | Valid values: all, avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url, username (optional) (default to fullName, username)

try:
    # Update Membership of Member on a Board
    api_instance.put_boards_id_memberships_idmembership(id, id_membership, type, member_fields=member_fields)
except ApiException as e:
    print("Exception when calling DefaultApi->put_boards_id_memberships_idmembership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The id of the board to update | 
 **id_membership** | [**TrelloID**](.md)| The id of a membership that should be added to this board. | 
 **type** | **str**| One of: admin, normal, observer. Determines the type of member that this membership will be to this board. | 
 **member_fields** | **str**| Valid values: all, avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url, username | [optional] [default to fullName, username]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_boards_id_my_prefs_showlistguide**
> put_boards_id_my_prefs_showlistguide(id, value)

Update showListGuide Pref on a Board

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The id of the board to update
value = true # bool | Determines whether to show the list guide.

try:
    # Update showListGuide Pref on a Board
    api_instance.put_boards_id_my_prefs_showlistguide(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->put_boards_id_my_prefs_showlistguide: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The id of the board to update | 
 **value** | **bool**| Determines whether to show the list guide. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_boards_id_my_prefs_showsidebar**
> put_boards_id_my_prefs_showsidebar(id, value)

Update showSidebar Pref on a Board

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The id of the board to update
value = true # bool | Determines whether to show the side bar.

try:
    # Update showSidebar Pref on a Board
    api_instance.put_boards_id_my_prefs_showsidebar(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->put_boards_id_my_prefs_showsidebar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The id of the board to update | 
 **value** | **bool**| Determines whether to show the side bar. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_boards_id_my_prefs_showsidebaractivity**
> put_boards_id_my_prefs_showsidebaractivity(id, value)

Update showSidebarActivity Pref on a Board

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The id of the board to update
value = true # bool | Determines whether to show sidebar activity.

try:
    # Update showSidebarActivity Pref on a Board
    api_instance.put_boards_id_my_prefs_showsidebaractivity(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->put_boards_id_my_prefs_showsidebaractivity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The id of the board to update | 
 **value** | **bool**| Determines whether to show sidebar activity. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_boards_id_my_prefs_showsidebarboardactions**
> put_boards_id_my_prefs_showsidebarboardactions(id, value)

Update showSidebarBoardActions Pref on a Board

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The id of the board to update
value = true # bool | Determines whether to show the sidebar board actions.

try:
    # Update showSidebarBoardActions Pref on a Board
    api_instance.put_boards_id_my_prefs_showsidebarboardactions(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->put_boards_id_my_prefs_showsidebarboardactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The id of the board to update | 
 **value** | **bool**| Determines whether to show the sidebar board actions. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_boards_id_my_prefs_showsidebarmembers**
> put_boards_id_my_prefs_showsidebarmembers(id, value)

Update showSidebarMembers Pref on a Board

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The id of the board to update
value = true # bool | Determines whether to show members of the board in the sidebar.

try:
    # Update showSidebarMembers Pref on a Board
    api_instance.put_boards_id_my_prefs_showsidebarmembers(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->put_boards_id_my_prefs_showsidebarmembers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The id of the board to update | 
 **value** | **bool**| Determines whether to show members of the board in the sidebar. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_boards_id_myprefs_emailposition**
> put_boards_id_myprefs_emailposition(id, value)

Update emailPosition Pref on a Board

Update emailPosition Pref on a Board

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The id of the board to update
value = 'value_example' # str | Valid values: bottom, top. Determines the position of the email address.

try:
    # Update emailPosition Pref on a Board
    api_instance.put_boards_id_myprefs_emailposition(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->put_boards_id_myprefs_emailposition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The id of the board to update | 
 **value** | **str**| Valid values: bottom, top. Determines the position of the email address. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_boards_id_myprefs_idemaillist**
> put_boards_id_myprefs_idemaillist(id, value)

Update idEmailList Pref on a Board

Change the default list that email-to-board cards are created in.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The id of the board to update
value = trello_api_client.TrelloID() # TrelloID | The id of an email list.

try:
    # Update idEmailList Pref on a Board
    api_instance.put_boards_id_myprefs_idemaillist(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->put_boards_id_myprefs_idemaillist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The id of the board to update | 
 **value** | [**TrelloID**](.md)| The id of an email list. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_cards_id**
> Card put_cards_id(id, name=name, desc=desc, closed=closed, id_members=id_members, id_attachment_cover=id_attachment_cover, id_list=id_list, id_labels=id_labels, id_board=id_board, pos=pos, due=due, start=start, due_complete=due_complete, subscribed=subscribed, address=address, location_name=location_name, coordinates=coordinates, cover=cover)

Update a Card

Update a card

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
name = 'name_example' # str | The new name for the card (optional)
desc = 'desc_example' # str | The new description for the card (optional)
closed = true # bool | Whether the card should be archived (closed: true) (optional)
id_members = trello_api_client.TrelloID() # TrelloID | Comma-separated list of member IDs (optional)
id_attachment_cover = trello_api_client.TrelloID() # TrelloID | The ID of the image attachment the card should use as its cover, or null for none (optional)
id_list = trello_api_client.TrelloID() # TrelloID | The ID of the list the card should be in (optional)
id_labels = trello_api_client.TrelloID() # TrelloID | Comma-separated list of label IDs (optional)
id_board = trello_api_client.TrelloID() # TrelloID | The ID of the board the card should be on (optional)
pos = trello_api_client.Pos1() # Pos1 | The position of the card in its list. `top`, `bottom`, or a positive float (optional)
due = '2013-10-20' # date | When the card is due, or `null` (optional)
start = '2013-10-20' # date | The start date of a card, or `null` (optional)
due_complete = true # bool | Whether the due date should be marked complete (optional)
subscribed = true # bool | Whether the member is should be subscribed to the card (optional)
address = 'address_example' # str | For use with/by the Map View (optional)
location_name = 'location_name_example' # str | For use with/by the Map View (optional)
coordinates = 'coordinates_example' # str | For use with/by the Map View. Should be latitude,longitude (optional)
cover = trello_api_client.Cover() # Cover | Updates the card's cover  | Option | Values | About |  |--------|--------|-------|  | color | `pink`, `yellow`, `lime`, `blue`, `black`, `orange`, `red`, `purple`, `sky`, `green` | Makes the cover a solid color . |  | brightness | `dark`, `light` | Determines whether the text on the cover should be dark or light.  | url | An unsplash URL: https://images.unsplash.com | Used if making an image the cover. Only Unsplash URLs work.  | idAttachment | ID of an attachment on the card | Used if setting an attached image as the cover. |  | size | `normal`, `full` | Determines whether to show the card name on the cover, or below it. |    `brightness` can be sent alongside any of the other parameters, but all of the other parameters are mutually exclusive; you can not have the cover be a `color` and an `idAttachment` at the same time.     On the brightness options, setting it to light will make the text on the card cover dark:  ![](/cloud/trello/images/rest/cards/cover-brightness-dark.png)    And vice versa, setting it to dark will make the text on the card cover light:   ![](/cloud/trello/images/rest/cards/cover-brightness-light.png)  (optional)

try:
    # Update a Card
    api_response = api_instance.put_cards_id(id, name=name, desc=desc, closed=closed, id_members=id_members, id_attachment_cover=id_attachment_cover, id_list=id_list, id_labels=id_labels, id_board=id_board, pos=pos, due=due, start=start, due_complete=due_complete, subscribed=subscribed, address=address, location_name=location_name, coordinates=coordinates, cover=cover)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_cards_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **name** | **str**| The new name for the card | [optional] 
 **desc** | **str**| The new description for the card | [optional] 
 **closed** | **bool**| Whether the card should be archived (closed: true) | [optional] 
 **id_members** | [**TrelloID**](.md)| Comma-separated list of member IDs | [optional] 
 **id_attachment_cover** | [**TrelloID**](.md)| The ID of the image attachment the card should use as its cover, or null for none | [optional] 
 **id_list** | [**TrelloID**](.md)| The ID of the list the card should be in | [optional] 
 **id_labels** | [**TrelloID**](.md)| Comma-separated list of label IDs | [optional] 
 **id_board** | [**TrelloID**](.md)| The ID of the board the card should be on | [optional] 
 **pos** | [**Pos1**](.md)| The position of the card in its list. &#x60;top&#x60;, &#x60;bottom&#x60;, or a positive float | [optional] 
 **due** | **date**| When the card is due, or &#x60;null&#x60; | [optional] 
 **start** | **date**| The start date of a card, or &#x60;null&#x60; | [optional] 
 **due_complete** | **bool**| Whether the due date should be marked complete | [optional] 
 **subscribed** | **bool**| Whether the member is should be subscribed to the card | [optional] 
 **address** | **str**| For use with/by the Map View | [optional] 
 **location_name** | **str**| For use with/by the Map View | [optional] 
 **coordinates** | **str**| For use with/by the Map View. Should be latitude,longitude | [optional] 
 **cover** | [**Cover**](.md)| Updates the card&#x27;s cover  | Option | Values | About |  |--------|--------|-------|  | color | &#x60;pink&#x60;, &#x60;yellow&#x60;, &#x60;lime&#x60;, &#x60;blue&#x60;, &#x60;black&#x60;, &#x60;orange&#x60;, &#x60;red&#x60;, &#x60;purple&#x60;, &#x60;sky&#x60;, &#x60;green&#x60; | Makes the cover a solid color . |  | brightness | &#x60;dark&#x60;, &#x60;light&#x60; | Determines whether the text on the cover should be dark or light.  | url | An unsplash URL: https://images.unsplash.com | Used if making an image the cover. Only Unsplash URLs work.  | idAttachment | ID of an attachment on the card | Used if setting an attached image as the cover. |  | size | &#x60;normal&#x60;, &#x60;full&#x60; | Determines whether to show the card name on the cover, or below it. |    &#x60;brightness&#x60; can be sent alongside any of the other parameters, but all of the other parameters are mutually exclusive; you can not have the cover be a &#x60;color&#x60; and an &#x60;idAttachment&#x60; at the same time.     On the brightness options, setting it to light will make the text on the card cover dark:  ![](/cloud/trello/images/rest/cards/cover-brightness-dark.png)    And vice versa, setting it to dark will make the text on the card cover light:   ![](/cloud/trello/images/rest/cards/cover-brightness-light.png)  | [optional] 

### Return type

[**Card**](Card.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_cards_id_actions_idaction_comments**
> put_cards_id_actions_idaction_comments(id, id_action, text)

Update Comment Action on a Card

Update an existing comment

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
id_action = trello_api_client.TrelloID() # TrelloID | The ID of the comment action to update
text = 'text_example' # str | The new text for the comment

try:
    # Update Comment Action on a Card
    api_instance.put_cards_id_actions_idaction_comments(id, id_action, text)
except ApiException as e:
    print("Exception when calling DefaultApi->put_cards_id_actions_idaction_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **id_action** | [**TrelloID**](.md)| The ID of the comment action to update | 
 **text** | **str**| The new text for the comment | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_cards_id_checkitem_idcheckitem**
> put_cards_id_checkitem_idcheckitem(id, id_check_item, name=name, state=state, id_checklist=id_checklist, pos=pos, due=due, due_reminder=due_reminder, id_member=id_member)

Update a checkItem on a Card

Update an item in a checklist on a card.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
id_check_item = trello_api_client.TrelloID() # TrelloID | The ID of the checkitem
name = 'name_example' # str | The new name for the checklist item (optional)
state = 'state_example' # str | One of: `complete`, `incomplete` (optional)
id_checklist = trello_api_client.TrelloID() # TrelloID | The ID of the checklist this item is in (optional)
pos = trello_api_client.PosStringOrNumber() # PosStringOrNumber | `top`, `bottom`, or a positive float (optional)
due = '2013-10-20' # date | A due date for the checkitem (optional)
due_reminder = 1.2 # float | A dueReminder for the due date on the checkitem (optional)
id_member = trello_api_client.TrelloID() # TrelloID | The ID of the member to remove from the card (optional)

try:
    # Update a checkItem on a Card
    api_instance.put_cards_id_checkitem_idcheckitem(id, id_check_item, name=name, state=state, id_checklist=id_checklist, pos=pos, due=due, due_reminder=due_reminder, id_member=id_member)
except ApiException as e:
    print("Exception when calling DefaultApi->put_cards_id_checkitem_idcheckitem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **id_check_item** | [**TrelloID**](.md)| The ID of the checkitem | 
 **name** | **str**| The new name for the checklist item | [optional] 
 **state** | **str**| One of: &#x60;complete&#x60;, &#x60;incomplete&#x60; | [optional] 
 **id_checklist** | [**TrelloID**](.md)| The ID of the checklist this item is in | [optional] 
 **pos** | [**PosStringOrNumber**](.md)| &#x60;top&#x60;, &#x60;bottom&#x60;, or a positive float | [optional] 
 **due** | **date**| A due date for the checkitem | [optional] 
 **due_reminder** | **float**| A dueReminder for the due date on the checkitem | [optional] 
 **id_member** | [**TrelloID**](.md)| The ID of the member to remove from the card | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_cards_id_stickers_idsticker**
> put_cards_id_stickers_idsticker(id, id_sticker, top, left, z_index, rotate=rotate)

Update a Sticker on a Card

Update a sticker on a card

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Card
id_sticker = trello_api_client.TrelloID() # TrelloID | The ID of the sticker
top = 3.4 # float | The top position of the sticker, from -60 to 100
left = 3.4 # float | The left position of the sticker, from -60 to 100
z_index = 56 # int | The z-index of the sticker
rotate = 0 # float | The rotation of the sticker (optional) (default to 0)

try:
    # Update a Sticker on a Card
    api_instance.put_cards_id_stickers_idsticker(id, id_sticker, top, left, z_index, rotate=rotate)
except ApiException as e:
    print("Exception when calling DefaultApi->put_cards_id_stickers_idsticker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Card | 
 **id_sticker** | [**TrelloID**](.md)| The ID of the sticker | 
 **top** | **float**| The top position of the sticker, from -60 to 100 | 
 **left** | **float**| The left position of the sticker, from -60 to 100 | 
 **z_index** | **int**| The z-index of the sticker | 
 **rotate** | **float**| The rotation of the sticker | [optional] [default to 0]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_cards_idcard_checklist_idchecklist_checkitem_idcheckitem**
> CheckItem put_cards_idcard_checklist_idchecklist_checkitem_idcheckitem(id_card, id_check_item, id_checklist, pos=pos)

Update Checkitem on Checklist on Card

Update an item in a checklist on a card.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id_card = trello_api_client.TrelloID() # TrelloID | The ID of the Card
id_check_item = trello_api_client.TrelloID() # TrelloID | The ID of the checklist item to update
id_checklist = trello_api_client.TrelloID() # TrelloID | The ID of the item to update.
pos = trello_api_client.PosStringOrNumber() # PosStringOrNumber | `top`, `bottom`, or a positive float (optional)

try:
    # Update Checkitem on Checklist on Card
    api_response = api_instance.put_cards_idcard_checklist_idchecklist_checkitem_idcheckitem(id_card, id_check_item, id_checklist, pos=pos)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_cards_idcard_checklist_idchecklist_checkitem_idcheckitem: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_card** | [**TrelloID**](.md)| The ID of the Card | 
 **id_check_item** | [**TrelloID**](.md)| The ID of the checklist item to update | 
 **id_checklist** | [**TrelloID**](.md)| The ID of the item to update. | 
 **pos** | [**PosStringOrNumber**](.md)| &#x60;top&#x60;, &#x60;bottom&#x60;, or a positive float | [optional] 

### Return type

[**CheckItem**](CheckItem.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_cards_idcard_customfield_idcustomfield_item**
> put_cards_idcard_customfield_idcustomfield_item(id_card, id_custom_field, body=body)

Update Custom Field item on Card

Setting, updating, and removing the value for a Custom Field on a card. For more details on updating custom fields check out the [Getting Started With Custom Fields](/cloud/trello/guides/rest-api/getting-started-with-custom-fields/)

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id_card = trello_api_client.TrelloID() # TrelloID | ID of the card that the Custom Field value should be set/updated for
id_custom_field = trello_api_client.TrelloID() # TrelloID | ID of the Custom Field on the card.
body = trello_api_client.IdCustomFieldItemBody() # IdCustomFieldItemBody |  (optional)

try:
    # Update Custom Field item on Card
    api_instance.put_cards_idcard_customfield_idcustomfield_item(id_card, id_custom_field, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->put_cards_idcard_customfield_idcustomfield_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_card** | [**TrelloID**](.md)| ID of the card that the Custom Field value should be set/updated for | 
 **id_custom_field** | [**TrelloID**](.md)| ID of the Custom Field on the card. | 
 **body** | [**IdCustomFieldItemBody**](IdCustomFieldItemBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_cards_idcard_customfields**
> put_cards_idcard_customfields(body=body)

Update Multiple Custom Field items on Card

Setting, updating, and removing the values for multiple Custom Fields on a card. For more details on updating custom fields check out the [Getting Started With Custom Fields](/cloud/trello/guides/rest-api/getting-started-with-custom-fields/)

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
body = trello_api_client.IdCardCustomFieldsBody() # IdCardCustomFieldsBody |  (optional)

try:
    # Update Multiple Custom Field items on Card
    api_instance.put_cards_idcard_customfields(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->put_cards_idcard_customfields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdCardCustomFieldsBody**](IdCardCustomFieldsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_checklists_id_field**
> put_checklists_id_field(id, field, value)

Update field on a Checklist

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of a checklist.
field = 'field_example' # str | Field to update.
value = trello_api_client.Value() # Value | The value to change the checklist name to. Should be a string of length 1 to 16384.

try:
    # Update field on a Checklist
    api_instance.put_checklists_id_field(id, field, value)
except ApiException as e:
    print("Exception when calling DefaultApi->put_checklists_id_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of a checklist. | 
 **field** | **str**| Field to update. | 
 **value** | [**Value**](.md)| The value to change the checklist name to. Should be a string of length 1 to 16384. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_checlists_id**
> put_checlists_id(id, name=name, pos=pos)

Update a Checklist

Update an existing checklist.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of a checklist.
name = 'name_example' # str | Name of the new checklist being created. Should be length of 1 to 16384. (optional)
pos = trello_api_client.PosStringOrNumber() # PosStringOrNumber | Determines the position of the checklist on the card. One of: `top`, `bottom`, or a positive number. (optional)

try:
    # Update a Checklist
    api_instance.put_checlists_id(id, name=name, pos=pos)
except ApiException as e:
    print("Exception when calling DefaultApi->put_checlists_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of a checklist. | 
 **name** | **str**| Name of the new checklist being created. Should be length of 1 to 16384. | [optional] 
 **pos** | [**PosStringOrNumber**](.md)| Determines the position of the checklist on the card. One of: &#x60;top&#x60;, &#x60;bottom&#x60;, or a positive number. | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_customfields_id**
> CustomField put_customfields_id(id, body=body)

Update a Custom Field definition

Update a Custom Field definition.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the Custom Field.
body = trello_api_client.CustomFieldsIdBody() # CustomFieldsIdBody |  (optional)

try:
    # Update a Custom Field definition
    api_response = api_instance.put_customfields_id(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_customfields_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the Custom Field. | 
 **body** | [**CustomFieldsIdBody**](CustomFieldsIdBody.md)|  | [optional] 

### Return type

[**CustomField**](CustomField.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_enterprises_id_admins_idmember**
> put_enterprises_id_admins_idmember(id, id_member)

Update Member to be admin of Enterprise

Make Member an admin of Enterprise.   NOTE: This endpoint is not available to enterprises that have opted in to user management via AdminHub.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the enterprise to retrieve.
id_member = trello_api_client.TrelloID() # TrelloID | ID of member to be made an admin of enterprise.

try:
    # Update Member to be admin of Enterprise
    api_instance.put_enterprises_id_admins_idmember(id, id_member)
except ApiException as e:
    print("Exception when calling DefaultApi->put_enterprises_id_admins_idmember: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the enterprise to retrieve. | 
 **id_member** | [**TrelloID**](.md)| ID of member to be made an admin of enterprise. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_enterprises_id_enterprise_join_request_bulk**
> put_enterprises_id_enterprise_join_request_bulk(id, id_organizations)

Decline enterpriseJoinRequests from one organization or a bulk list of organizations.

Decline enterpriseJoinRequests from one organization or bulk amount of organizations

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the Enterprise to retrieve.
id_organizations = NULL # list[object] | An array of IDs of an Organization resource.

try:
    # Decline enterpriseJoinRequests from one organization or a bulk list of organizations.
    api_instance.put_enterprises_id_enterprise_join_request_bulk(id, id_organizations)
except ApiException as e:
    print("Exception when calling DefaultApi->put_enterprises_id_enterprise_join_request_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the Enterprise to retrieve. | 
 **id_organizations** | [**list[object]**](object.md)| An array of IDs of an Organization resource. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_enterprises_id_members_idmember_licensed**
> Member put_enterprises_id_members_idmember_licensed(id, id_member, value)

Update a Member's licensed status

This endpoint is used to update whether the provided Member should use one of the Enterprise's available licenses or not. Revoking a license will deactivate a Member of an Enterprise.    NOTE: Revoking of licenses is not possible for enterprises that have opted in to user management via AdminHub.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the Enterprise.
id_member = trello_api_client.TrelloID() # TrelloID | The ID of the Member
value = true # bool | Boolean value to determine whether the user should be given an Enterprise license (true) or not (false).

try:
    # Update a Member's licensed status
    api_response = api_instance.put_enterprises_id_members_idmember_licensed(id, id_member, value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_enterprises_id_members_idmember_licensed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the Enterprise. | 
 **id_member** | [**TrelloID**](.md)| The ID of the Member | 
 **value** | **bool**| Boolean value to determine whether the user should be given an Enterprise license (true) or not (false). | 

### Return type

[**Member**](Member.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_enterprises_id_organizations**
> list[object] put_enterprises_id_organizations(id, id_organization)

Transfer an Organization to an Enterprise.

Transfer an organization to an enterprise.   NOTE: For enterprises that have opted in to user management via AdminHub, this endpoint will result in the organization being added to the enterprise asynchronously. A 200 response only indicates receipt of the request, it does not indicate successful addition to the enterprise.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the Enterprise to retrieve.
id_organization = 'id_organization_example' # str | ID of Organization to be transferred to Enterprise.

try:
    # Transfer an Organization to an Enterprise.
    api_response = api_instance.put_enterprises_id_organizations(id, id_organization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_enterprises_id_organizations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the Enterprise to retrieve. | 
 **id_organization** | **str**| ID of Organization to be transferred to Enterprise. | 

### Return type

**list[object]**

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_id_idboard**
> put_id_idboard(id, value)

Move List to Board

Move a List to a different Board

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the list
value = trello_api_client.TrelloID() # TrelloID | The ID of the board to move the list to

try:
    # Move List to Board
    api_instance.put_id_idboard(id, value)
except ApiException as e:
    print("Exception when calling DefaultApi->put_id_idboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the list | 
 **value** | [**TrelloID**](.md)| The ID of the board to move the list to | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_labels_id**
> put_labels_id(id, name=name, color=color)

Update a Label

Update a label by ID.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the Label
name = 'name_example' # str | The new name for the label (optional)
color = trello_api_client.Color() # Color | The new color for the label. See: [fields](/cloud/trello/guides/rest-api/object-definitions/) for color options (optional)

try:
    # Update a Label
    api_instance.put_labels_id(id, name=name, color=color)
except ApiException as e:
    print("Exception when calling DefaultApi->put_labels_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the Label | 
 **name** | **str**| The new name for the label | [optional] 
 **color** | [**Color**](.md)| The new color for the label. See: [fields](/cloud/trello/guides/rest-api/object-definitions/) for color options | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_labels_id_field**
> put_labels_id_field(id, field, value)

Update a field on a label

Update a field on a label.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = 'id_example' # str | The id of the label
field = 'field_example' # str | The field on the Label to update.
value = trello_api_client.TrelloID() # TrelloID | The new value for the field.

try:
    # Update a field on a label
    api_instance.put_labels_id_field(id, field, value)
except ApiException as e:
    print("Exception when calling DefaultApi->put_labels_id_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the label | 
 **field** | **str**| The field on the Label to update. | 
 **value** | [**TrelloID**](.md)| The new value for the field. | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_lists_id**
> put_lists_id(id, name=name, closed=closed, id_board=id_board, pos=pos, subscribed=subscribed)

Update a List

Update the properties of a List

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = 'id_example' # str | The ID of the list
name = 'name_example' # str | New name for the list (optional)
closed = true # bool | Whether the list should be closed (archived) (optional)
id_board = trello_api_client.TrelloID() # TrelloID | ID of a board the list should be moved to (optional)
pos = trello_api_client.Pos2() # Pos2 | New position for the list: `top`, `bottom`, or a positive floating point number (optional)
subscribed = true # bool | Whether the active member is subscribed to this list (optional)

try:
    # Update a List
    api_instance.put_lists_id(id, name=name, closed=closed, id_board=id_board, pos=pos, subscribed=subscribed)
except ApiException as e:
    print("Exception when calling DefaultApi->put_lists_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the list | 
 **name** | **str**| New name for the list | [optional] 
 **closed** | **bool**| Whether the list should be closed (archived) | [optional] 
 **id_board** | [**TrelloID**](.md)| ID of a board the list should be moved to | [optional] 
 **pos** | [**Pos2**](.md)| New position for the list: &#x60;top&#x60;, &#x60;bottom&#x60;, or a positive floating point number | [optional] 
 **subscribed** | **bool**| Whether the active member is subscribed to this list | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_lists_id_closed**
> put_lists_id_closed(id, value=value)

Archive or unarchive a list

Archive or unarchive a list

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the list
value = trello_api_client.TrelloID() # TrelloID | Set to true to close (archive) the list (optional)

try:
    # Archive or unarchive a list
    api_instance.put_lists_id_closed(id, value=value)
except ApiException as e:
    print("Exception when calling DefaultApi->put_lists_id_closed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the list | 
 **value** | [**TrelloID**](.md)| Set to true to close (archive) the list | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_lists_id_field**
> put_lists_id_field(id, field, value=value)

Update a field on a List

Rename a list

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the list
field = 'field_example' # str | The field on the List to be updated
value = trello_api_client.Value1() # Value1 | The new value for the field (optional)

try:
    # Update a field on a List
    api_instance.put_lists_id_field(id, field, value=value)
except ApiException as e:
    print("Exception when calling DefaultApi->put_lists_id_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the list | 
 **field** | **str**| The field on the List to be updated | 
 **value** | [**Value1**](.md)| The new value for the field | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_members_id**
> InlineResponse2001 put_members_id(id, full_name=full_name, initials=initials, username=username, bio=bio, avatar_source=avatar_source, prefscolor_blind=prefscolor_blind, prefslocale=prefslocale, prefsminutes_between_summaries=prefsminutes_between_summaries)

Update a Member

Update a Member

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member
full_name = 'full_name_example' # str | New name for the member. Cannot begin or end with a space. (optional)
initials = 'initials_example' # str | New initials for the member. 1-4 characters long. (optional)
username = 'username_example' # str | New username for the member. At least 3 characters long, only lowercase letters, underscores, and numbers. Must be unique. (optional)
bio = 'bio_example' # str |  (optional)
avatar_source = 'avatar_source_example' # str | One of: `gravatar`, `none`, `upload` (optional)
prefscolor_blind = true # bool |  (optional)
prefslocale = 'prefslocale_example' # str |  (optional)
prefsminutes_between_summaries = 56 # int | `-1` for disabled, `1`, or `60` (optional)

try:
    # Update a Member
    api_response = api_instance.put_members_id(id, full_name=full_name, initials=initials, username=username, bio=bio, avatar_source=avatar_source, prefscolor_blind=prefscolor_blind, prefslocale=prefslocale, prefsminutes_between_summaries=prefsminutes_between_summaries)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_members_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 
 **full_name** | **str**| New name for the member. Cannot begin or end with a space. | [optional] 
 **initials** | **str**| New initials for the member. 1-4 characters long. | [optional] 
 **username** | **str**| New username for the member. At least 3 characters long, only lowercase letters, underscores, and numbers. Must be unique. | [optional] 
 **bio** | **str**|  | [optional] 
 **avatar_source** | **str**| One of: &#x60;gravatar&#x60;, &#x60;none&#x60;, &#x60;upload&#x60; | [optional] 
 **prefscolor_blind** | **bool**|  | [optional] 
 **prefslocale** | **str**|  | [optional] 
 **prefsminutes_between_summaries** | **int**| &#x60;-1&#x60; for disabled, &#x60;1&#x60;, or &#x60;60&#x60; | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_members_id_boardbackgrounds_idbackground**
> BoardBackground put_members_id_boardbackgrounds_idbackground(id, id_background, brightness=brightness, tile=tile)

Update a Member's custom Board background

Update a board background

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member
id_background = trello_api_client.TrelloID() # TrelloID | The ID of the board background
brightness = 'brightness_example' # str | One of: `dark`, `light`, `unknown` (optional)
tile = true # bool | Whether the background should be tiled (optional)

try:
    # Update a Member's custom Board background
    api_response = api_instance.put_members_id_boardbackgrounds_idbackground(id, id_background, brightness=brightness, tile=tile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_members_id_boardbackgrounds_idbackground: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 
 **id_background** | [**TrelloID**](.md)| The ID of the board background | 
 **brightness** | **str**| One of: &#x60;dark&#x60;, &#x60;light&#x60;, &#x60;unknown&#x60; | [optional] 
 **tile** | **bool**| Whether the background should be tiled | [optional] 

### Return type

[**BoardBackground**](BoardBackground.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_members_id_boardstars_idstar**
> put_members_id_boardstars_idstar(id, id_star, pos=pos)

Update the position of a boardStar of Member

Update the position of a starred board

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or username of the member
id_star = trello_api_client.TrelloID() # TrelloID | The ID of the board star
pos = trello_api_client.PosStringOrNumber() # PosStringOrNumber | New position for the starred board. `top`, `bottom`, or a positive float. (optional)

try:
    # Update the position of a boardStar of Member
    api_instance.put_members_id_boardstars_idstar(id, id_star, pos=pos)
except ApiException as e:
    print("Exception when calling DefaultApi->put_members_id_boardstars_idstar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or username of the member | 
 **id_star** | [**TrelloID**](.md)| The ID of the board star | 
 **pos** | [**PosStringOrNumber**](.md)| New position for the starred board. &#x60;top&#x60;, &#x60;bottom&#x60;, or a positive float. | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_members_id_customboardbackgrounds_idbackground**
> BoardBackground put_members_id_customboardbackgrounds_idbackground(id, id_background, brightness=brightness, tile=tile)

Update custom Board Background of Member

Update a specific custom board background

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.Id2() # Id2 | The ID or username of the member
id_background = trello_api_client.TrelloID() # TrelloID | The ID of the custom background
brightness = 'brightness_example' # str | One of: `dark`, `light`, `unknown` (optional)
tile = true # bool | Whether to tile the background (optional)

try:
    # Update custom Board Background of Member
    api_response = api_instance.put_members_id_customboardbackgrounds_idbackground(id, id_background, brightness=brightness, tile=tile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_members_id_customboardbackgrounds_idbackground: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id2**](.md)| The ID or username of the member | 
 **id_background** | [**TrelloID**](.md)| The ID of the custom background | 
 **brightness** | **str**| One of: &#x60;dark&#x60;, &#x60;light&#x60;, &#x60;unknown&#x60; | [optional] 
 **tile** | **bool**| Whether to tile the background | [optional] 

### Return type

[**BoardBackground**](BoardBackground.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_members_id_notification_channel_settings_channel_blocked_keys**
> NotificationChannelSettings put_members_id_notification_channel_settings_channel_blocked_keys(body, id)

Update blocked notification keys of Member on a channel

Update blocked notification keys of Member on a specific channel

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
body = trello_api_client.IdNotificationsChannelSettingsBody() # IdNotificationsChannelSettingsBody | 
id = trello_api_client.Id3() # Id3 | The ID or username of the member

try:
    # Update blocked notification keys of Member on a channel
    api_response = api_instance.put_members_id_notification_channel_settings_channel_blocked_keys(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_members_id_notification_channel_settings_channel_blocked_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdNotificationsChannelSettingsBody**](IdNotificationsChannelSettingsBody.md)|  | 
 **id** | [**Id3**](.md)| The ID or username of the member | 

### Return type

[**NotificationChannelSettings**](NotificationChannelSettings.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_members_id_notification_channel_settings_channel_blocked_keys_0**
> NotificationChannelSettings put_members_id_notification_channel_settings_channel_blocked_keys_0(body, id, channel)

Update blocked notification keys of Member on a channel

Update blocked notification keys of Member on a specific channel

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
body = trello_api_client.NotificationsChannelSettingsChannelBody() # NotificationsChannelSettingsChannelBody | 
id = trello_api_client.Id4() # Id4 | The ID or username of the member
channel = trello_api_client.Channel() # Channel | Channel to block notifications on

try:
    # Update blocked notification keys of Member on a channel
    api_response = api_instance.put_members_id_notification_channel_settings_channel_blocked_keys_0(body, id, channel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_members_id_notification_channel_settings_channel_blocked_keys_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationsChannelSettingsChannelBody**](NotificationsChannelSettingsChannelBody.md)|  | 
 **id** | [**Id4**](.md)| The ID or username of the member | 
 **channel** | [**Channel**](.md)| Channel to block notifications on | 

### Return type

[**NotificationChannelSettings**](NotificationChannelSettings.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_members_id_notification_channel_settings_channel_blocked_keys_1**
> NotificationChannelSettings put_members_id_notification_channel_settings_channel_blocked_keys_1(id, channel, blocked_keys)

Update blocked notification keys of Member on a channel

Update blocked notification keys of Member on a specific channel

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.Id5() # Id5 | The ID or username of the member
channel = trello_api_client.Channel() # Channel | Channel to block notifications on
blocked_keys = trello_api_client.BlockedKey() # BlockedKey | Singular key or comma-separated list of notification keys

try:
    # Update blocked notification keys of Member on a channel
    api_response = api_instance.put_members_id_notification_channel_settings_channel_blocked_keys_1(id, channel, blocked_keys)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_members_id_notification_channel_settings_channel_blocked_keys_1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id5**](.md)| The ID or username of the member | 
 **channel** | [**Channel**](.md)| Channel to block notifications on | 
 **blocked_keys** | [**BlockedKey**](.md)| Singular key or comma-separated list of notification keys | 

### Return type

[**NotificationChannelSettings**](NotificationChannelSettings.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_members_id_savedsearches_idsearch**
> SavedSearch put_members_id_savedsearches_idsearch(id, id_search, name=name, query=query, pos=pos)

Update a saved search

Update a saved search

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = 'id_example' # str | The ID or username of the member
id_search = 'id_search_example' # str | The ID of the saved search to delete
name = 'name_example' # str | The new name for the saved search (optional)
query = 'query_example' # str | The new search query (optional)
pos = 'pos_example' # str | New position for saves search. `top`, `bottom`, or a positive float. (optional)

try:
    # Update a saved search
    api_response = api_instance.put_members_id_savedsearches_idsearch(id, id_search, name=name, query=query, pos=pos)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_members_id_savedsearches_idsearch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID or username of the member | 
 **id_search** | **str**| The ID of the saved search to delete | 
 **name** | **str**| The new name for the saved search | [optional] 
 **query** | **str**| The new search query | [optional] 
 **pos** | **str**| New position for saves search. &#x60;top&#x60;, &#x60;bottom&#x60;, or a positive float. | [optional] 

### Return type

[**SavedSearch**](SavedSearch.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_notifications_id**
> InlineResponse2002 put_notifications_id(id, unread=unread)

Update a Notification's read status

Update the read status of a notification

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the notification
unread = true # bool | Whether the notification should be marked as read or not (optional)

try:
    # Update a Notification's read status
    api_response = api_instance.put_notifications_id(id, unread=unread)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_notifications_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the notification | 
 **unread** | **bool**| Whether the notification should be marked as read or not | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_notifications_id_unread**
> InlineResponse2002 put_notifications_id_unread(id, value=value)

Update Notification's read status

Update Notification's read status

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID of the notification
value = 'value_example' # str |  (optional)

try:
    # Update Notification's read status
    api_response = api_instance.put_notifications_id_unread(id, value=value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_notifications_id_unread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID of the notification | 
 **value** | **str**|  | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_organizations_id**
> Organization put_organizations_id(id, name=name, display_name=display_name, desc=desc, website=website, prefsassociated_domain=prefsassociated_domain, prefsexternal_members_disabled=prefsexternal_members_disabled, prefsgoogle_apps_version=prefsgoogle_apps_version, prefsboard_visibility_restrictorg=prefsboard_visibility_restrictorg, prefsboard_visibility_restrictprivate=prefsboard_visibility_restrictprivate, prefsboard_visibility_restrictpublic=prefsboard_visibility_restrictpublic, prefsorg_invite_restrict=prefsorg_invite_restrict, prefspermission_level=prefspermission_level)

Update an Organization

Update an organization

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or name of the Organization
name = 'name_example' # str | A new name for the organization. At least 3 lowercase letters, underscores, and numbers. Must be unique (optional)
display_name = 'display_name_example' # str | A new displayName for the organization. Must be at least 1 character long and not begin or end with a space. (optional)
desc = 'desc_example' # str | A new description for the organization (optional)
website = 'website_example' # str | A URL starting with `http://`, `https://`, or `null` (optional)
prefsassociated_domain = 'prefsassociated_domain_example' # str | The Google Apps domain to link this org to. (optional)
prefsexternal_members_disabled = true # bool | Whether non-workspace members can be added to boards inside the Workspace (optional)
prefsgoogle_apps_version = 56 # int | `1` or `2` (optional)
prefsboard_visibility_restrictorg = 'prefsboard_visibility_restrictorg_example' # str | Who on the Workspace can make Workspace visible boards. One of `admin`, `none`, `org` (optional)
prefsboard_visibility_restrictprivate = 'prefsboard_visibility_restrictprivate_example' # str | Who can make private boards. One of: `admin`, `none`, `org` (optional)
prefsboard_visibility_restrictpublic = 'prefsboard_visibility_restrictpublic_example' # str | Who on the Workspace can make public boards. One of: `admin`, `none`, `org` (optional)
prefsorg_invite_restrict = 'prefsorg_invite_restrict_example' # str | An email address with optional wildcard characters. (E.g. `subdomain.*.trello.com`) (optional)
prefspermission_level = 'prefspermission_level_example' # str | Whether the Workspace page is publicly visible. One of: `private`, `public` (optional)

try:
    # Update an Organization
    api_response = api_instance.put_organizations_id(id, name=name, display_name=display_name, desc=desc, website=website, prefsassociated_domain=prefsassociated_domain, prefsexternal_members_disabled=prefsexternal_members_disabled, prefsgoogle_apps_version=prefsgoogle_apps_version, prefsboard_visibility_restrictorg=prefsboard_visibility_restrictorg, prefsboard_visibility_restrictprivate=prefsboard_visibility_restrictprivate, prefsboard_visibility_restrictpublic=prefsboard_visibility_restrictpublic, prefsorg_invite_restrict=prefsorg_invite_restrict, prefspermission_level=prefspermission_level)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_organizations_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or name of the Organization | 
 **name** | **str**| A new name for the organization. At least 3 lowercase letters, underscores, and numbers. Must be unique | [optional] 
 **display_name** | **str**| A new displayName for the organization. Must be at least 1 character long and not begin or end with a space. | [optional] 
 **desc** | **str**| A new description for the organization | [optional] 
 **website** | **str**| A URL starting with &#x60;http://&#x60;, &#x60;https://&#x60;, or &#x60;null&#x60; | [optional] 
 **prefsassociated_domain** | **str**| The Google Apps domain to link this org to. | [optional] 
 **prefsexternal_members_disabled** | **bool**| Whether non-workspace members can be added to boards inside the Workspace | [optional] 
 **prefsgoogle_apps_version** | **int**| &#x60;1&#x60; or &#x60;2&#x60; | [optional] 
 **prefsboard_visibility_restrictorg** | **str**| Who on the Workspace can make Workspace visible boards. One of &#x60;admin&#x60;, &#x60;none&#x60;, &#x60;org&#x60; | [optional] 
 **prefsboard_visibility_restrictprivate** | **str**| Who can make private boards. One of: &#x60;admin&#x60;, &#x60;none&#x60;, &#x60;org&#x60; | [optional] 
 **prefsboard_visibility_restrictpublic** | **str**| Who on the Workspace can make public boards. One of: &#x60;admin&#x60;, &#x60;none&#x60;, &#x60;org&#x60; | [optional] 
 **prefsorg_invite_restrict** | **str**| An email address with optional wildcard characters. (E.g. &#x60;subdomain.*.trello.com&#x60;) | [optional] 
 **prefspermission_level** | **str**| Whether the Workspace page is publicly visible. One of: &#x60;private&#x60;, &#x60;public&#x60; | [optional] 

### Return type

[**Organization**](Organization.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_organizations_id_members**
> put_organizations_id_members(id, email, full_name, type=type)

Update an Organization's Members

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or name of the organization
email = 'email_example' # str | An email address
full_name = 'full_name_example' # str | Name for the member, at least 1 character not beginning or ending with a space
type = 'normal' # str | One of: `admin`, `normal` (optional) (default to normal)

try:
    # Update an Organization's Members
    api_instance.put_organizations_id_members(id, email, full_name, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->put_organizations_id_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or name of the organization | 
 **email** | **str**| An email address | 
 **full_name** | **str**| Name for the member, at least 1 character not beginning or ending with a space | 
 **type** | **str**| One of: &#x60;admin&#x60;, &#x60;normal&#x60; | [optional] [default to normal]

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_organizations_id_members_idmember**
> InlineResponse2001 put_organizations_id_members_idmember(id, id_member, type)

Update a Member of an Organization

Add a member to a Workspace or update their member type.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or name of the organization
id_member = trello_api_client.IdMember() # IdMember | The ID or username of the member to update
type = 'type_example' # str | One of: `admin`, `normal`

try:
    # Update a Member of an Organization
    api_response = api_instance.put_organizations_id_members_idmember(id, id_member, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_organizations_id_members_idmember: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or name of the organization | 
 **id_member** | [**IdMember**](.md)| The ID or username of the member to update | 
 **type** | **str**| One of: &#x60;admin&#x60;, &#x60;normal&#x60; | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_organizations_id_members_idmember_deactivated**
> put_organizations_id_members_idmember_deactivated(id, id_member, value)

Deactivate or reactivate a member of an Organization

Deactivate or reactivate a member of a Workspace

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or name of the organization
id_member = trello_api_client.IdMember1() # IdMember1 | The ID or username of the member to update
value = true # bool | 

try:
    # Deactivate or reactivate a member of an Organization
    api_instance.put_organizations_id_members_idmember_deactivated(id, id_member, value)
except ApiException as e:
    print("Exception when calling DefaultApi->put_organizations_id_members_idmember_deactivated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or name of the organization | 
 **id_member** | [**IdMember1**](.md)| The ID or username of the member to update | 
 **value** | **bool**|  | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_plugins_id**
> Plugin put_plugins_id(id)

Update a Plugin

Update a Plugin

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | The ID or name of the organization

try:
    # Update a Plugin
    api_response = api_instance.put_plugins_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_plugins_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| The ID or name of the organization | 

### Return type

[**Plugin**](Plugin.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_plugins_idplugin_listings_idlisting**
> PluginListing put_plugins_idplugin_listings_idlisting(id_plugin, id_listing, body=body)

Updating Plugin's Listing

Update an existing listing for your Power-Up

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id_plugin = trello_api_client.TrelloID() # TrelloID | The ID of the Power-Up whose listing is being updated.
id_listing = trello_api_client.TrelloID() # TrelloID | The ID of the existing listing for the Power-Up that is being updated.
body = trello_api_client.ListingsIdListingBody() # ListingsIdListingBody |  (optional)

try:
    # Updating Plugin's Listing
    api_response = api_instance.put_plugins_idplugin_listings_idlisting(id_plugin, id_listing, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_plugins_idplugin_listings_idlisting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_plugin** | [**TrelloID**](.md)| The ID of the Power-Up whose listing is being updated. | 
 **id_listing** | [**TrelloID**](.md)| The ID of the existing listing for the Power-Up that is being updated. | 
 **body** | [**ListingsIdListingBody**](ListingsIdListingBody.md)|  | [optional] 

### Return type

[**PluginListing**](PluginListing.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_webhooks_id**
> Webhook put_webhooks_id(id, description=description, callback_url=callback_url, id_model=id_model, active=active)

Update a Webhook

Update a webhook by ID.

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the webhook to retrieve.
description = 'description_example' # str | A string with a length from `0` to `16384`. (optional)
callback_url = 'callback_url_example' # str | A valid URL that is reachable with a `HEAD` and `POST` request. (optional)
id_model = trello_api_client.TrelloID() # TrelloID | ID of the model to be monitored (optional)
active = true # bool | Determines whether the webhook is active and sending `POST` requests. (optional)

try:
    # Update a Webhook
    api_response = api_instance.put_webhooks_id(id, description=description, callback_url=callback_url, id_model=id_model, active=active)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->put_webhooks_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the webhook to retrieve. | 
 **description** | **str**| A string with a length from &#x60;0&#x60; to &#x60;16384&#x60;. | [optional] 
 **callback_url** | **str**| A valid URL that is reachable with a &#x60;HEAD&#x60; and &#x60;POST&#x60; request. | [optional] 
 **id_model** | [**TrelloID**](.md)| ID of the model to be monitored | [optional] 
 **active** | **bool**| Determines whether the webhook is active and sending &#x60;POST&#x60; requests. | [optional] 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tokenstokenwebhooks1**
> tokenstokenwebhooks1(token, id_webhook, description=description, callback_url=callback_url, id_model=id_model)

Update a Webhook created by Token

Update a Webhook created by Token

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
token = 'token_example' # str | 
id_webhook = trello_api_client.TrelloID() # TrelloID | ID of the [Webhooks](ref:webhooks) to retrieve.
description = 'description_example' # str | A description to be displayed when retrieving information about the webhook. (optional)
callback_url = 'callback_url_example' # str | The URL that the webhook should `POST` information to. (optional)
id_model = trello_api_client.TrelloID() # TrelloID | ID of the object that the webhook is on. (optional)

try:
    # Update a Webhook created by Token
    api_instance.tokenstokenwebhooks1(token, id_webhook, description=description, callback_url=callback_url, id_model=id_model)
except ApiException as e:
    print("Exception when calling DefaultApi->tokenstokenwebhooks1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**|  | 
 **id_webhook** | [**TrelloID**](.md)| ID of the [Webhooks](ref:webhooks) to retrieve. | 
 **description** | **str**| A description to be displayed when retrieving information about the webhook. | [optional] 
 **callback_url** | **str**| The URL that the webhook should &#x60;POST&#x60; information to. | [optional] 
 **id_model** | [**TrelloID**](.md)| ID of the object that the webhook is on. | [optional] 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhooksidfield**
> webhooksidfield(id, field)

Get a field on a Webhook

Get a field on a Webhook

### Example
```python
from __future__ import print_function
import time
import trello_api_client
from trello_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: APIKey
configuration = trello_api_client.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'
# Configure API key authorization: APIToken
configuration = trello_api_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = trello_api_client.DefaultApi(trello_api_client.ApiClient(configuration))
id = trello_api_client.TrelloID() # TrelloID | ID of the webhook.
field = 'field_example' # str | Field to retrieve. One of: `active`, `callbackURL`, `description`, `idModel`

try:
    # Get a field on a Webhook
    api_instance.webhooksidfield(id, field)
except ApiException as e:
    print("Exception when calling DefaultApi->webhooksidfield: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**TrelloID**](.md)| ID of the webhook. | 
 **field** | **str**| Field to retrieve. One of: &#x60;active&#x60;, &#x60;callbackURL&#x60;, &#x60;description&#x60;, &#x60;idModel&#x60; | 

### Return type

void (empty response body)

### Authorization

[APIKey](../README.md#APIKey), [APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

