---
description: "Seam is a universal API for smart locks, thermostats, access control systems, sensors and other connected building devices."
hidden: true
---

# Seam

<img src="../../.gitbook/assets/connectors/lg/seam.png" alt="Seam logo">

Seam is a universal API for smart locks, thermostats, access control systems, sensors and other connected building devices. This connector covers the Seam Connect API: devices, locks, thermostats, access codes, access grants, access methods, spaces, user identities, ACS systems and credentials, connected accounts, Connect Webviews, client sessions, phones, instant keys, noise sensors, events, action attempts, webhooks and workspaces.

| | |
| --- | --- |
| **Category** | [Developer tools](README.md) |
| **Website** | [getseam.com](https://getseam.com) |
| **Authentication** | Credentials you enter |
| **Slug** | `seam` |

## Use it

Add Seam from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.seam.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Activate Thermostat Climate Preset | `activateThermostatClimatePreset` | Activates a specified climate preset on a specified thermostat. Returns an action attempt that tracks the asynchronous device operation. |
| Add ACS User To Access Group | `addUserToAcsAccessGroup` | Adds a specified access system user to a specified access group. Provide either acs_user_id or user_identity_id, not both. |
| Add ACS User To Access Group By User | `addAcsUserToAccessGroup` | Adds a specified access system user to a specified access group, addressed from the user side. |
| Add ACS User To User Identity | `addAcsUserToUserIdentity` | Associates a specified access system user with a specified user identity. Identify the user identity by its ID or by your own user identity key. |
| Add Connected Account To Space | `addConnectedAccountToSpace` | Adds every device and entrance from a specified connected account to a specified space. |
| Add Devices To Space | `addDevicesToSpace` | Adds devices to a space without disturbing its existing members. |
| Add Entrances To Space | `addAcsEntrancesToSpace` | Adds one or more access system entrances to a specified space. |
| Assign Card To Access Method | `assignCardToAccessMethod` | Assigns a pre-registered card credential, identified by its card number, to a card-mode access method. |
| Assign Credential To ACS User | `assignAcsCredential` | Assigns a specified credential to a specified access system user. Provide either acs_user_id or user_identity_id, not both. |
| Configure Auto Lock | `configureAutoLock` | Enables or disables the auto-lock setting on a lock and sets the delay before it locks itself. When enabling auto-lock, auto_lock_delay_seconds is required. |

<details>

<summary>See 192 more actions</summary>

* **Convert Unmanaged Access Code To Managed** `convertUnmanagedAccessCodeToManaged`: Converts an unmanaged access code into an access code managed by Seam, enabling the full set of access code operations and lifecycle events for it.
* **Convert Unmanaged User Identity To Managed** `updateUnmanagedUserIdentity`: Converts an unmanaged user identity into a managed one by setting is_managed to true. The conversion cannot be reversed.
* **Create Access Code** `createAccessCode`: Creates a new access code on a single device. For granting access to a person, Seam recommends Access Grants instead; use this low-level endpoint when you need direct control over a code on one device, such as setting a custom PIN.
* **Create Access Grant** `createAccessGrant`: Creates a new Access Grant. Access Grants are the recommended way to give a person access to a physical space, whatever the underlying locking hardware. Specify either user_identity_id or a user_identity object.
* **Create ACS User** `createAcsUser`: Creates a new access system user in a specified access system, optionally with an access schedule and access group memberships.
* **Create Client Session** `createClientSession`: Creates a client session, the scoped, short-lived token your front end uses to talk to Seam on behalf of one of your users.
* **Create Connect Webview** `createConnectWebview`: Creates a Connect Webview, the hosted flow in which an end user signs in to their device or access system account so Seam can manage their devices.
* **Create Credential** `createAcsCredential`: Creates a new credential for a specified access system user. For most access use cases prefer Create Access Grant, which manages the underlying credentials for you; use this endpoint when you need direct control over an individual credential.
* **Create Customer Portal** `createCustomerPortal`: Creates a customer portal magic link that lets one of your customers manage their own Seam resources, with configurable features and locale.
* **Create Multiple Access Codes** `createMultipleAccessCodes`: Creates new access codes that share a common code across multiple devices, for example the same PIN on a front and back door lock.
* **Create Noise Threshold** `createNoiseThreshold`: Creates a noise threshold on a noise sensor, defining the noise level tolerated during a daily time window. One of noise_threshold_decibels or noise_threshold_nrs is required. The daily times use a time-of-day format with a region, such as 22:00:00[America/Los_Angeles], not a full date.
* **Create Space** `createSpace`: Creates a space, a named grouping of devices and entrances such as a unit, room or building.
* **Create Thermostat Climate Preset** `createThermostatClimatePreset`: Creates a reusable climate preset on a specified thermostat, defining the HVAC mode, fan mode and set points to apply when the preset is activated.
* **Create Thermostat Daily Program** `createThermostatDailyProgram`: Creates a thermostat daily program, a named set of periods that each activate a configured climate preset at a given time of day. Assign the program to days of the week with Update Thermostat Weekly Program.
* **Create Thermostat Schedule** `createThermostatSchedule`: Creates a thermostat schedule that activates a climate preset on a specified thermostat over a fixed time window. starts_at must be strictly before ends_at; equal timestamps are rejected.
* **Create User Identity** `createUserIdentity`: Creates a new user identity, the workspace-level record of a person who can be granted access across devices and access systems.
* **Create Webhook** `createWebhook`: Registers a new webhook endpoint that Seam posts events to. Use event_types to restrict which events are delivered, or leave it unset to receive all of them.
* **Create Workspace** `createWorkspace`: Creates a new Seam workspace, optionally a sandbox workspace for testing with virtual devices. Seam exposes no public endpoint to delete a workspace, so create one only when you intend to keep it.
* **Deactivate Phone** `deactivatePhone`: Deactivates a phone so its mobile keys stop working, for example when a user has lost their phone.
* **Delete Access Code** `deleteAccessCode`: Deletes a managed access code and removes it from the device.
* **Delete Access Grant** `deleteAccessGrant`: Deletes an access grant and revokes all access methods provisioned for it.
* **Delete Access Group** `deleteAcsAccessGroup`: Deletes a specified access group from its access control system.
* **Delete Access Method** `deleteAccessMethod`: Deletes an access method, or every access method belonging to an access grant.
* **Delete ACS User** `deleteAcsUser`: Deletes a specified access system user and invalidates their credentials. Provide either acs_user_id, or user_identity_id together with acs_system_id.
* **Delete Client Session** `deleteClientSession`: Deletes a client session and its record. Revoking a session is a separate action.
* **Delete Connect Webview** `deleteConnectWebview`: Deletes a Connect Webview. Completed Connect Webviews do not need to be deleted; you can simply ignore them.
* **Delete Connected Account** `deleteConnectedAccount`: Deletes a connected account and all data associated with it, including its devices and access codes. This emits a connected_account.deleted event.
* **Delete Credential** `deleteAcsCredential`: Deletes a specified access system credential.
* **Delete Customer Data** `deleteCustomerData`: Deletes a customer's pushed data and the Seam resources derived from it, such as user identities, access grants and spaces. This is irreversible.
* **Delete Instant Key** `deleteInstantKey`: Deletes a specified Instant Key so its shareable link stops granting access.
* **Delete Noise Threshold** `deleteNoiseThreshold`: Deletes a noise threshold from a noise sensor.
* **Delete Space** `deleteSpace`: Deletes a space. The devices and entrances it contained are not deleted, only their membership of the space.
* **Delete Thermostat Climate Preset** `deleteThermostatClimatePreset`: Deletes a specified climate preset from a specified thermostat.
* **Delete Thermostat Daily Program** `deleteThermostatDailyProgram`: Deletes a specified thermostat daily program.
* **Delete Thermostat Schedule** `deleteThermostatSchedule`: Deletes a specified thermostat schedule.
* **Delete Unmanaged Access Code** `deleteUnmanagedAccessCode`: Deletes an unmanaged access code from the device.
* **Delete User Identity** `deleteUserIdentity`: Deletes a specified user identity together with all associated resources, including its credentials, access system users and client sessions.
* **Delete Webhook** `deleteWebhook`: Deletes a specified webhook endpoint so Seam stops posting events to it.
* **Encode Access Method** `encodeAccessMethod`: Encodes an existing access method onto a plastic card placed on the specified encoder.
* **Encode Credential** `encodeAcsEncoderCredential`: Encodes an existing credential onto a plastic card placed on a specified encoder. Provide either acs_credential_id or access_method_id. Returns an action attempt that tracks the asynchronous encoding.
* **Generate Access Code** `generateAccessCode`: Generates a valid code value for a device without creating an access code, so you can preview the PIN a device would accept.
* **Generate Instant Key For User Identity** `generateUserIdentityInstantKey`: Generates a new instant key for a specified user identity, a shareable web link that lets the holder unlock the doors they have access to.
* **Get Access Code** `getAccessCode`: Returns a specified access code. Specify either access_code_id, or both device_id and code.
* **Get Access Grant** `getAccessGrant`: Returns a specified access grant. Specify either access_grant_id or access_grant_key.
* **Get Access Grant Related Resources** `getAccessGrantRelatedResources`: Returns one or more access grants together with their related resources, such as access methods, devices, entrances and spaces.
* **Get Access Group** `getAcsAccessGroup`: Returns a specified access group, including its access schedule, external type and workspace.
* **Get Access Method** `getAccessMethod`: Returns a specified access method.
* **Get Access Method Related Resources** `getAccessMethodRelatedResources`: Returns one or more access methods together with their related resources, such as access grants, devices and entrances.
* **Get ACS System** `getAcsSystem`: Returns a specified access control system connected to the workspace.
* **Get ACS User** `getAcsUser`: Returns a specified access system user. Provide either acs_user_id, or user_identity_id together with acs_system_id.
* **Get Action Attempt** `getActionAttempt`: Returns a specified action attempt so you can poll the progress of an asynchronous operation such as a lock or unlock.
* **Get Client Session** `getClientSession`: Returns a specified client session. Specify either client_session_id or user_identifier_key.
* **Get Connect Webview** `getConnectWebview`: Returns a specified Connect Webview. Poll it to find out whether the user has signed in and which devices they connected.
* **Get Connected Account** `getConnectedAccount`: Returns a specified connected account. Specify either connected_account_id or email.
* **Get Credential** `getAcsCredential`: Returns a specified access system credential, the means by which an access system user gains access at an entrance.
* **Get Device** `getDevice`: Returns a specified device. Specify either device_id or name.
* **Get Encoder** `getAcsEncoder`: Returns a specified card encoder, the hardware device that writes credential data onto physical key cards.
* **Get Entrance** `getAcsEntrance`: Returns a specified access system entrance, the secured door, gate or zone controlled by an access system.
* **Get Event** `getEvent`: Returns a specified event, the same payload Seam would deliver by webhook, so you can retrieve an event that already took place. Note: when the event does not exist Seam still answers with a success status and a body of {"message":"Event not found","ok":true}, so check for the event fields rather than relying on the status code.
* **Get Instant Key** `getInstantKey`: Returns a specified Instant Key. Specify either instant_key_id or instant_key_url.
* **Get Lock** `getLock`: Returns a specified lock and its current locked state. Specify either device_id or name.
* **Get Noise Threshold** `getNoiseThreshold`: Returns a specified noise threshold.
* **Get Or Create Client Session** `getOrCreateClientSession`: Returns a client session matching the given characteristics, creating it first if no such session exists.
* **Get Phone** `getPhone`: Returns a specified phone registered as a mobile-key device.
* **Get Space** `getSpace`: Returns a specified space. Specify either space_id or space_key.
* **Get Space Related Resources** `getSpaceRelatedResources`: Returns one or more spaces together with their related resources, such as devices, entrances and access grants.
* **Get Thermostat Schedule** `getThermostatSchedule`: Returns a specified thermostat schedule.
* **Get Unmanaged Access Code** `getUnmanagedAccessCode`: Returns a specified unmanaged access code. Specify either access_code_id, or both device_id and code.
* **Get Unmanaged Access Grant** `getUnmanagedAccessGrant`: Returns a specified unmanaged access grant, that is, one whose is_managed flag is false.
* **Get Unmanaged Access Method** `getUnmanagedAccessMethod`: Returns a specified unmanaged access method, that is, one whose is_managed flag is false.
* **Get Unmanaged Device** `getUnmanagedDevice`: Returns a specified unmanaged device. Unmanaged devices expose a limited set of properties and events and cannot be controlled.
* **Get Unmanaged User Identity** `getUnmanagedUserIdentity`: Returns a specified unmanaged user identity, that is one where is_managed is false.
* **Get User Identity** `getUserIdentity`: Returns a specified user identity, addressed by its ID or by your own user identity key.
* **Get Webhook** `getWebhook`: Returns a specified webhook endpoint.
* **Get Workspace** `getWorkspace`: Returns the Seam workspace that the configured API key belongs to.
* **Grant Access To Client Session** `grantAccessToClientSession`: Grants an existing client session access to additional resources, such as Connect Webviews, connected accounts or user identities.
* **Grant ACS User Access To Entrance** `grantAcsEntranceAccess`: Grants a specified access system user access to a specified entrance. Provide either acs_user_id or user_identity_id, not both.
* **Grant User Identity Access To Device** `grantUserIdentityAccessToDevice`: Grants a specified user identity access to a specified managed device.
* **List Access Codes** `listAccessCodes`: Returns a list of access codes. You must specify one of device_id, access_code_ids, access_method_id, access_grant_id or access_grant_key.
* **List Access Grants** `listAccessGrants`: Returns a list of access grants in the workspace, optionally filtered by user identity, access system, entrance, device, space, access code or reservation.
* **List Access Groups** `listAcsAccessGroups`: Returns a list of all access groups in the workspace, optionally filtered by access system, access system user, user identity or a search term.
* **List Access Methods** `listAccessMethods`: Returns the access methods provisioned for an access grant or entrance, such as PIN codes, cards, mobile keys and cloud keys.
* **List ACS Systems** `listAcsSystems`: Returns a list of all access control systems connected to the workspace, optionally filtered by connected account, customer key or a search term.
* **List ACS Systems For User Identity** `listUserIdentityAcsSystems`: Returns all access control systems associated with a specified user identity.
* **List ACS Users** `listAcsUsers`: Returns a list of all access system users in the workspace, optionally filtered by access system, user identity or a search term.
* **List ACS Users For User Identity** `listUserIdentityAcsUsers`: Returns all access system users assigned to a specified user identity.
* **List ACS Users In Access Group** `listAcsAccessGroupUsers`: Returns a list of all access system users that belong to a specified access group.
* **List Action Attempts** `listActionAttempts`: Returns the action attempts that you specify by ID, or those for a given device.
* **List Client Sessions** `listClientSessions`: Returns the client sessions in the workspace, optionally filtered by user identity, user identifier key or Connect Webview.
* **List Compatible Credential Manager ACS Systems** `listCompatibleCredentialManagerAcsSystems`: Returns a list of all credential manager systems that are compatible with a specified access system.
* **List Connect Webviews** `listConnectWebviews`: Returns the Connect Webviews created in the workspace.
* **List Connected Accounts** `listConnectedAccounts`: Returns the device or access system accounts that end users have connected to the workspace.
* **List Credentials** `listAcsCredentials`: Returns access system credentials in the workspace. One of acs_user_id, acs_system_id or user_identity_id is required to scope the list; a search term can narrow it further. (A client session token is the only way to list without scoping.)
* **List Credentials With Access To Entrance** `listAcsEntranceCredentialsWithAccess`: Returns a list of all credentials that grant access to a specified entrance.
* **List Device Providers** `listDeviceProviders`: Returns the device providers Seam supports, each with its capability flags such as whether it can be remotely unlocked.
* **List Devices** `listDevices`: Returns a list of all devices in the Seam workspace.
* **List Devices Accessible To User Identity** `listUserIdentityAccessibleDevices`: Returns all devices a specified user identity can access, including devices from its access grants and devices linked directly to the identity.
* **List Encoders** `listAcsEncoders`: Returns card encoders in the workspace. One of acs_system_id, acs_system_ids or acs_encoder_ids is required to scope the list.
* **List Entrances** `listAcsEntrances`: Returns a list of all access system entrances in the workspace, optionally filtered by access system, credential, access method, space, connected account or a search term.
* **List Entrances Accessible To Access Group** `listAcsAccessGroupAccessibleEntrances`: Returns a list of all entrances that members of a specified access group can access.
* **List Entrances Accessible To ACS User** `listAcsUserAccessibleEntrances`: Lists the entrances to which a specified access system user has access. Provide either acs_user_id, or user_identity_id together with acs_system_id.
* **List Entrances Accessible To Credential** `listAcsCredentialAccessibleEntrances`: Returns a list of all entrances to which a specified credential grants access.
* **List Entrances Accessible To User Identity** `listUserIdentityAccessibleEntrances`: Returns all access system entrances a specified user identity can access, including entrances from its access grants and from its linked access system users.
* **List Events** `listEvents`: Returns the events that have occurred in the workspace, the same events Seam delivers by webhook. You must supply either since or between.
* **List Instant Keys** `listInstantKeys`: Returns the Instant Keys issued in the workspace. An Instant Key is a shareable web link that grants a guest access without installing an app.
* **List Locks** `listLocks`: Returns a list of the smart locks in the workspace, optionally filtered by device type or manufacturer.
* **List Noise Sensors** `listNoiseSensors`: Returns the noise sensors in the workspace, optionally filtered by device type or manufacturer.
* **List Noise Thresholds** `listNoiseThresholds`: Returns the noise thresholds configured on a noise sensor.
* **List Phones** `listPhones`: Returns the phones registered as mobile-key devices, optionally filtered by owner user identity or credential.
* **List Spaces** `listSpaces`: Returns the spaces in the workspace, optionally filtered by customer, space key, parent space, connected account or a free-text search.
* **List Thermostat Schedules** `listThermostatSchedules`: Returns a list of all thermostat schedules for a specified thermostat.
* **List Thermostats** `listThermostats`: Returns a list of all thermostat devices in the workspace, optionally filtered by connected account, Connect Webview, device type or manufacturer.
* **List Unmanaged Access Codes** `listUnmanagedAccessCodes`: Returns the unmanaged access codes programmed on a device, that is, codes that exist on the lock but are not managed by Seam.
* **List Unmanaged Access Grants** `listUnmanagedAccessGrants`: Returns the unmanaged access grants in the workspace, that is, those whose is_managed flag is false.
* **List Unmanaged Access Methods** `listUnmanagedAccessMethods`: Returns the unmanaged access methods for an access grant, that is, those whose is_managed flag is false.
* **List Unmanaged Devices** `listUnmanagedDevices`: Returns a list of unmanaged devices, that is, devices visible to Seam but not under its management.
* **List Unmanaged User Identities** `listUnmanagedUserIdentities`: Returns a list of all unmanaged user identities, that is those where is_managed is false.
* **List User Identities** `listUserIdentities`: Returns a list of all user identities in the workspace, optionally filtered by ID, credential manager or a search term.
* **List Webhooks** `listWebhooks`: Returns all webhook endpoints registered in the workspace.
* **List Workspaces** `listWorkspaces`: Returns the Seam workspaces that the configured API key can access.
* **Lock Door** `lockDoor`: Locks a smart lock. This physically actuates the door lock, so use it only against a device you are entitled to control. Returns an action attempt tracking the operation.
* **Merge User Identities** `mergeUserIdentities`: Merges one or more duplicate user identities into a primary user identity. The merged identities are deleted and their resources move to the primary identity.
* **Pull Backup Access Code** `pullBackupAccessCode`: Retrieves a backup access code from the device's backup code pool for a time-bound access code, so access can continue if the primary code fails.
* **Push Customer Data** `pushCustomerData`: Pushes a customer's property-management data into Seam, including spaces, properties, rooms, units, listings, reservations, guests, users and access grants.
* **Remove ACS User From Access Group** `removeUserFromAcsAccessGroup`: Removes a specified access system user from a specified access group.
* **Remove ACS User From Access Group By User** `removeAcsUserFromAccessGroup`: Removes a specified access system user from a specified access group, addressed from the user side. Provide either acs_user_id or user_identity_id.
* **Remove ACS User From User Identity** `removeAcsUserFromUserIdentity`: Removes the association between a specified access system user and a specified user identity.
* **Remove Connected Account From Space** `removeConnectedAccountFromSpace`: Removes every device and entrance belonging to a specified connected account from a specified space.
* **Remove Devices From Space** `removeDevicesFromSpace`: Removes devices from a space without deleting the devices themselves.
* **Remove Entrances From Space** `removeAcsEntrancesFromSpace`: Removes one or more access system entrances from a specified space.
* **Report Access Code Device Constraints** `reportAccessCodeDeviceConstraints`: Reports access-code constraints for a device, such as the code lengths it supports. Specify either supported_code_lengths or min_code_length and max_code_length.
* **Report ACS System Devices** `reportAcsSystemDevices`: Reports the current encoders and entrances present on a specified access system, so that Seam can reconcile its view of the system hardware.
* **Report Device Provider Metadata** `reportDeviceProviderMetadata`: Updates provider-specific metadata for one or more devices.
* **Request Access Methods** `requestAccessMethods`: Adds additional requested access methods, such as a PIN code, card or mobile key, to an existing access grant.
* **Reset Sandbox Workspace** `resetSandboxWorkspace`: Resets the sandbox workspace associated with the configured API key, clearing its virtual devices and data. Available only for sandbox workspaces.
* **Revoke ACS User Access To All Entrances** `revokeAcsUserAccessToAllEntrances`: Revokes access to every entrance for a specified access system user. Provide either acs_user_id, or user_identity_id together with acs_system_id.
* **Revoke Client Session** `revokeClientSession`: Revokes a client session so its token stops working, without deleting the session record.
* **Revoke User Identity Access To Device** `revokeUserIdentityAccessToDevice`: Revokes a specified user identity's access to a specified managed device.
* **Scan Credential** `scanAcsEncoderCredential`: Scans an encoded credential from a plastic card placed on a specified encoder. Returns an action attempt that tracks the asynchronous scan.
* **Scan To Assign Credential** `scanAcsEncoderToAssignCredential`: Scans a physical card placed on a specified encoder and assigns the scanned credential to an access system user. Provide either acs_user_id or user_identity_id.
* **Set Thermostat Fallback Climate Preset** `setThermostatFallbackClimatePreset`: Sets a specified climate preset as the fallback preset for a thermostat, applied whenever no schedule is active.
* **Set Thermostat Fan Mode** `setThermostatFanMode`: Sets the fan mode setting for a specified thermostat.
* **Set Thermostat HVAC Mode** `setThermostatHvacMode`: Sets the HVAC mode for a specified thermostat, together with the set points that the chosen mode requires.
* **Set Thermostat Temperature Threshold** `setThermostatTemperatureThreshold`: Sets a temperature threshold for a specified thermostat. Seam emits a thermostat.temperature_threshold_exceeded event and adds a warning when the device reports a temperature outside the range.
* **Set Thermostat To Cool Mode** `coolThermostat`: Sets a specified thermostat to cool mode at a given cooling set point. Provide the set point in either Celsius or Fahrenheit.
* **Set Thermostat To Heat Mode** `heatThermostat`: Sets a specified thermostat to heat mode at a given heating set point. Provide the set point in either Celsius or Fahrenheit.
* **Set Thermostat To Heat-Cool Mode** `heatCoolThermostat`: Sets a specified thermostat to heat-cool (auto) mode with both a heating and a cooling set point. Provide the set points in either Celsius or Fahrenheit.
* **Set Thermostat To Off Mode** `offThermostat`: Turns off heating and cooling on a specified thermostat by setting it to off mode.
* **Simulate Connect Device** `simulateConnectDevice`: Simulates a device connecting to Seam. Applies only to virtual devices in a Seam sandbox workspace.
* **Simulate Connect Device To Hub** `simulateConnectDeviceToHub`: Simulates a device's Wi-Fi hub or bridge coming back online, clearing the hub_disconnected error. Sandbox workspaces only, currently for August and TTLock locks.
* **Simulate Create Sandbox Phone** `simulateCreateSandboxPhone`: Creates a simulated phone for a user identity so you can test mobile keys. Available only in a Seam sandbox workspace.
* **Simulate Create Unmanaged Access Code** `simulateCreateUnmanagedAccessCode`: Simulates the creation of an unmanaged access code on a virtual device. Available only in a Seam sandbox workspace.
* **Simulate Disconnect Connected Account** `simulateDisconnectConnectedAccount`: Simulates a connected account becoming disconnected from Seam. Applies only to sandbox workspaces.
* **Simulate Disconnect Device** `simulateDisconnectDevice`: Simulates a device disconnecting from Seam, so you can test how your app handles device disconnection. Applies only to virtual devices in a Seam sandbox workspace.
* **Simulate Disconnect Device From Hub** `simulateDisconnectDeviceFromHub`: Simulates a device's Wi-Fi hub or bridge going offline. Sandbox workspaces only, currently for August, TTLock and IglooHome devices.
* **Simulate Keypad Code Entry** `simulateKeypadCodeEntry`: Simulates a PIN code being entered on a lock's keypad. Applies only to August devices in a Seam sandbox workspace.
* **Simulate Manual Lock Via Keypad** `simulateManualLockViaKeypad`: Simulates someone locking a door manually at the keypad. Applies only to August devices in a Seam sandbox workspace.
* **Simulate Next Credential Encode Will Fail** `simulateNextAcsEncoderCredentialEncodeWillFail`: Simulates that the next attempt to encode a credential using a specified encoder will fail. Available only in a sandbox workspace.
* **Simulate Next Credential Encode Will Succeed** `simulateNextAcsEncoderCredentialEncodeWillSucceed`: Simulates that the next attempt to encode a credential using a specified encoder will succeed. Available only in a sandbox workspace.
* **Simulate Next Credential Scan Will Fail** `simulateNextAcsEncoderCredentialScanWillFail`: Simulates that the next attempt to scan a credential using a specified encoder will fail. Available only in a sandbox workspace.
* **Simulate Next Credential Scan Will Succeed** `simulateNextAcsEncoderCredentialScanWillSucceed`: Simulates that the next attempt to scan a credential using a specified encoder will succeed. Available only in a sandbox workspace.
* **Simulate Paid Device Subscription** `simulatePaidDeviceSubscription`: Toggles a simulated paid provider subscription, such as Nuki Smart Hosting, for a device. Sandbox workspaces only.
* **Simulate Remove Device** `simulateRemoveDevice`: Simulates a device being removed from Seam, so you can test how your app handles device removal. Applies only to virtual devices in a Seam sandbox workspace.
* **Simulate Thermostat HVAC Mode Adjusted** `simulateThermostatHvacModeAdjusted`: Simulates a person having adjusted the HVAC mode on a thermostat. Applies only to sandbox devices.
* **Simulate Thermostat Temperature Reached** `simulateThermostatTemperatureReached`: Simulates a thermostat reaching a specified temperature. Applies only to sandbox devices.
* **Simulate Trigger Noise Threshold** `simulateTriggerNoiseThreshold`: Simulates a noise threshold being exceeded on a noise sensor. Available only in a Seam sandbox workspace.
* **Suspend ACS User** `suspendAcsUser`: Suspends a specified access system user, temporarily revoking their access. Use Unsuspend ACS User to restore it.
* **Sync Connected Account** `syncConnectedAccount`: Requests a fresh sync of a connected account so Seam pulls its current devices and state from the provider.
* **Unassign Credential From ACS User** `unassignAcsCredential`: Unassigns a specified credential from a specified access system user. Provide either acs_user_id or user_identity_id, not both.
* **Unlock Access Method Door** `unlockAccessMethodDoor`: Remotely unlocks an entrance using the cloud key credential associated with an access method. Returns an action attempt that tracks the unlock operation.
* **Unlock Door** `unlockDoor`: Unlocks a smart lock. This physically actuates the door lock, so use it only against a device you are entitled to control. Returns an action attempt tracking the operation.
* **Unlock Entrance** `unlockAcsEntrance`: Remotely unlocks a specified entrance using a cloud key credential. Returns an action attempt that tracks the progress of the unlock operation.
* **Unsuspend ACS User** `unsuspendAcsUser`: Unsuspends a specified suspended access system user, restoring their access.
* **Update Access Code** `updateAccessCode`: Updates an active or upcoming access code, for example to change its PIN, name or validity window.
* **Update Access Grant** `updateAccessGrant`: Updates an existing access grant's name and validity window. Specify either access_grant_id or access_grant_key.
* **Update ACS User** `updateAcsUser`: Updates the properties of a specified access system user, such as their name, contact details or access schedule.
* **Update Connected Account** `updateConnectedAccount`: Updates a connected account, for example its display name, customer, accepted capabilities or custom metadata.
* **Update Credential** `updateAcsCredential`: Updates the access code and the end of the validity period for a specified access system credential.
* **Update Device** `updateDevice`: Updates a device: rename it, attach custom metadata, toggle its backup access code pool, or convert a managed device to unmanaged.
* **Update Multiple Access Codes** `updateMultipleAccessCodes`: Updates every access code in a linked group that shares the given common code key, across all of their devices. At least one of name, starts_at or ends_at must be supplied, otherwise the request is rejected.
* **Update Noise Threshold** `updateNoiseThreshold`: Updates a noise threshold on a noise sensor, for example its decibel limit or daily active window.
* **Update Space** `updateSpace`: Updates an existing space. Supplying device_ids or acs_entrance_ids replaces the space's current membership.
* **Update Thermostat Climate Preset** `updateThermostatClimatePreset`: Updates an existing climate preset on a specified thermostat.
* **Update Thermostat Daily Program** `updateThermostatDailyProgram`: Updates a specified thermostat daily program. The periods that you supply replace all existing periods on the program.
* **Update Thermostat Schedule** `updateThermostatSchedule`: Updates a specified thermostat schedule, such as its window, climate preset or override permissions.
* **Update Thermostat Weekly Program** `updateThermostatWeeklyProgram`: Updates the weekly program for a thermostat by assigning a daily program to each day of the week. Days you omit are cleared.
* **Update Unmanaged Access Code** `updateUnmanagedAccessCode`: Updates the Seam-side settings of an unmanaged access code, such as whether it is managed or externally modifiable.
* **Update Unmanaged Access Grant** `updateUnmanagedAccessGrant`: Converts an unmanaged access grant into one managed by Seam. is_managed must be set to true.
* **Update Unmanaged Device** `updateUnmanagedDevice`: Updates an unmanaged device. Set is_managed to true to convert it into a device managed by Seam.
* **Update User Identity** `updateUserIdentity`: Updates the name, contact details or key of a specified user identity.
* **Update Webhook** `updateWebhook`: Updates the event types that a webhook endpoint subscribes to.
* **Update Workspace** `updateWorkspace`: Updates the workspace that the configured API key belongs to, for example its name, Connect Webview branding or publishable key setting.

</details>

## Events

Start a workflow when one of these happens, with an [app event trigger](../../build/triggers/README.md).

| Event | Id | When it fires |
| --- | --- | --- |
| Access Code Backup Access Code Pulled | `access_code.backup_access_code_pulled` | A backup access code was pulled from the backup pool and set on a device. |
| Access Code Changed | `access_code.changed` | An access code was changed. |
| Access Code Code Changed | `access_code.code_changed` | The PIN code of an access code was changed on the device. |
| Access Code Created | `access_code.created` | An access code was created. |
| Access Code Delay In Issuing | `access_code.delay_in_issuing` | Seam has not yet issued this access code even though its start time is approaching. |
| Access Code Delay In Removing From Device | `access_code.delay_in_removing_from_device` | There was an unusually long delay in removing an access code from a device. |
| Access Code Delay In Setting On Device | `access_code.delay_in_setting_on_device` | There was an unusually long delay in setting an access code on a device. |
| Access Code Deleted | `access_code.deleted` | An access code was deleted. |
| Access Code Deleted External To Seam | `access_code.deleted_external_to_seam` | An access code was deleted outside of Seam. |
| Access Code Failed To Issue | `access_code.failed_to_issue` | Seam was unable to issue this access code before its start time. |

<details>

<summary>See 104 more events</summary>

* **Access Code Failed To Remove** `access_code.failed_to_remove`: An access code is still active on the device even though its end time has passed.
* **Access Code Failed To Remove From Device** `access_code.failed_to_remove_from_device`: An access code failed to be removed from a device.
* **Access Code Failed To Set On Device** `access_code.failed_to_set_on_device`: An access code failed to be set on a device.
* **Access Code Failed To Update** `access_code.failed_to_update`: Seam was unable to apply this access code's requested update to the device.
* **Access Code Issued** `access_code.issued`: An access code was issued.
* **Access Code Modified External To Seam** `access_code.modified_external_to_seam`: An access code was modified outside of Seam.
* **Access Code Mutations Requested** `access_code.mutations_requested`: Mutations were requested on an access code, before the change is confirmed on the device.
* **Access Code Name Changed** `access_code.name_changed`: The name of an access code was changed on the device.
* **Access Code Removed From Device** `access_code.removed_from_device`: An access code was removed from a device.
* **Access Code Scheduled On Device** `access_code.scheduled_on_device`: An access code was scheduled natively on a device.
* **Access Code Set On Device** `access_code.set_on_device`: An access code was set on a device.
* **Access Code Time Frame Changed** `access_code.time_frame_changed`: The time frame of an access code was changed on the device.
* **Access Grant Access Granted To All Doors** `access_grant.access_granted_to_all_doors`: All access requested for an access grant was successfully granted.
* **Access Grant Access Granted To Door** `access_grant.access_granted_to_door`: Access to a particular door requested as part of an access grant was successfully granted.
* **Access Grant Access Times Changed** `access_grant.access_times_changed`: An access grant's start or end time was changed.
* **Access Grant Access To Door Lost** `access_grant.access_to_door_lost`: Access to a particular door that was requested as part of an access grant was lost.
* **Access Grant Could Not Create Requested Access Methods** `access_grant.could_not_create_requested_access_methods`: One or more requested access methods could not be created for an access grant.
* **Access Grant Created** `access_grant.created`: An access grant was created.
* **Access Grant Deleted** `access_grant.deleted`: An access grant was deleted.
* **Access Method Card Encoding Required** `access_method.card_encoding_required`: An access method representing a physical card requires encoding.
* **Access Method Created** `access_method.created`: An access method was created.
* **Access Method Delay In Issuing** `access_method.delay_in_issuing`: Seam has not yet issued this access method even though its access grant is about to begin.
* **Access Method Deleted** `access_method.deleted`: An access method was deleted.
* **Access Method Failed To Issue** `access_method.failed_to_issue`: Seam was unable to issue this access method before its access grant started.
* **Access Method Issued** `access_method.issued`: An access method was issued.
* **Access Method Reissued** `access_method.reissued`: An access method was reissued.
* **Access Method Revoked** `access_method.revoked`: An access method was revoked.
* **ACS Access Group Deleted** `acs_access_group.deleted`: An access system access group was deleted.
* **ACS Credential Deleted** `acs_credential.deleted`: An access system credential was deleted.
* **ACS Credential Invalidated** `acs_credential.invalidated`: An access system credential was invalidated and can no longer be used.
* **ACS Credential Issued** `acs_credential.issued`: An access system credential was issued.
* **ACS Credential Reissued** `acs_credential.reissued`: An access system credential was reissued.
* **ACS Encoder Added** `acs_encoder.added`: An access system encoder was added.
* **ACS Encoder Removed** `acs_encoder.removed`: An access system encoder was removed.
* **ACS Entrance Added** `acs_entrance.added`: An access system entrance was added.
* **ACS Entrance Removed** `acs_entrance.removed`: An access system entrance was removed.
* **ACS System Added** `acs_system.added`: An access system was added.
* **ACS System Connected** `acs_system.connected`: An access system was connected.
* **ACS System Disconnected** `acs_system.disconnected`: An access system was disconnected.
* **ACS User Created** `acs_user.created`: An access system user was created.
* **ACS User Deleted** `acs_user.deleted`: An access system user was deleted.
* **Action Attempt Lock Door Failed** `action_attempt.lock_door.failed`: A lock door action attempt failed.
* **Action Attempt Lock Door Succeeded** `action_attempt.lock_door.succeeded`: A lock door action attempt succeeded.
* **Action Attempt Simulate Keypad Code Entry Failed** `action_attempt.simulate_keypad_code_entry.failed`: A simulate keypad code entry action attempt failed.
* **Action Attempt Simulate Keypad Code Entry Succeeded** `action_attempt.simulate_keypad_code_entry.succeeded`: A simulate keypad code entry action attempt succeeded.
* **Action Attempt Simulate Manual Lock Via Keypad Failed** `action_attempt.simulate_manual_lock_via_keypad.failed`: A simulate manual lock via keypad action attempt failed.
* **Action Attempt Simulate Manual Lock Via Keypad Succeeded** `action_attempt.simulate_manual_lock_via_keypad.succeeded`: A simulate manual lock via keypad action attempt succeeded.
* **Action Attempt Unlock Door Failed** `action_attempt.unlock_door.failed`: An unlock door action attempt failed.
* **Action Attempt Unlock Door Succeeded** `action_attempt.unlock_door.succeeded`: An unlock door action attempt succeeded.
* **Camera Activated** `camera.activated`: A camera was activated, for example by motion detection.
* **Client Session Deleted** `client_session.deleted`: A client session was deleted.
* **Connect Webview Login Failed** `connect_webview.login_failed`: A Connect Webview login failed.
* **Connect Webview Login Succeeded** `connect_webview.login_succeeded`: A Connect Webview login succeeded.
* **Connected Account Completed First Sync** `connected_account.completed_first_sync`: A connected account completed its first sync with Seam.
* **Connected Account Completed First Sync After Reconnection** `connected_account.completed_first_sync_after_reconnection`: A connected account completed its first sync after reconnection with Seam.
* **Connected Account Connected** `connected_account.connected`: A connected account was connected for the first time or reconnected after being disconnected.
* **Connected Account Created** `connected_account.created`: A connected account was created.
* **Connected Account Deleted** `connected_account.deleted`: A connected account was deleted.
* **Connected Account Disconnected** `connected_account.disconnected`: A connected account was disconnected.
* **Connected Account Reauthorization Requested** `connected_account.reauthorization_requested`: A connected account requires reauthorization using a new Connect Webview.
* **Connected Account Successful Login** `connected_account.successful_login`: A connected account had a successful login using a Connect Webview.
* **Device Accessory Keypad Connected** `device.accessory_keypad_connected`: An accessory keypad was connected to a device.
* **Device Accessory Keypad Disconnected** `device.accessory_keypad_disconnected`: An accessory keypad was disconnected from a device.
* **Device Added** `device.added`: A device was added to Seam or re-added after having been removed.
* **Device Battery Status Changed** `device.battery_status_changed`: A device battery status changed since the last battery status changed event.
* **Device Connected** `device.connected`: The status of a device changed from offline to online.
* **Device Connection Became Flaky** `device.connection_became_flaky`: Seam detected a flaky device connection.
* **Device Connection Stabilized** `device.connection_stabilized`: Seam detected that a previously flaky device connection stabilized.
* **Device Converted To Unmanaged** `device.converted_to_unmanaged`: A managed device was successfully converted to an unmanaged device.
* **Device Deleted** `device.deleted`: A device was deleted.
* **Device Disconnected** `device.disconnected`: The status of a device changed from online to offline.
* **Device Doorbell Rang** `device.doorbell_rang`: A doorbell button was pressed on a device.
* **Device Error Subscription Required** `device.error.subscription_required`: A third-party subscription is required to use all device features.
* **Device Error Subscription Required Resolved** `device.error.subscription_required.resolved`: A third-party subscription is active or no longer required to use all device features.
* **Device Low Battery** `device.low_battery`: A device battery level dropped below the low threshold.
* **Device Name Changed** `device.name_changed`: The name of a device was changed.
* **Device Removed** `device.removed`: A device was removed externally from the connected account.
* **Device Salto Privacy Mode Activated** `device.salto.privacy_mode_activated`: A Salto device activated privacy mode.
* **Device Salto Privacy Mode Deactivated** `device.salto.privacy_mode_deactivated`: A Salto device deactivated privacy mode.
* **Device Tampered** `device.tampered`: A device detected that it was tampered with, for example opened or moved.
* **Device Third Party Integration Detected** `device.third_party_integration_detected`: Seam detected that a device is using a third-party integration that interferes with device management.
* **Device Third Party Integration No Longer Detected** `device.third_party_integration_no_longer_detected`: Seam detected that a device is no longer using an interfering third-party integration.
* **Enrollment Automation Deleted** `enrollment_automation.deleted`: An enrollment automation was deleted.
* **Lock Access Denied** `lock.access_denied`: The lock denied access after one or more consecutive invalid attempts to unlock the device.
* **Lock Locked** `lock.locked`: A lock was locked.
* **Lock Unlocked** `lock.unlocked`: A lock was unlocked.
* **Noise Sensor Noise Threshold Triggered** `noise_sensor.noise_threshold_triggered`: Extended periods of noise or noise exceeding a threshold were detected.
* **Phone Deactivated** `phone.deactivated`: A phone device was deactivated.
* **Space Created** `space.created`: A space was created.
* **Space Deleted** `space.deleted`: A space was deleted.
* **Space Device Membership Changed** `space.device_membership_changed`: A device was added to or removed from a space.
* **Thermostat Climate Preset Activated** `thermostat.climate_preset_activated`: A thermostat climate preset was activated.
* **Thermostat Manually Adjusted** `thermostat.manually_adjusted`: A thermostat was adjusted manually.
* **Thermostat Temperature Changed** `thermostat.temperature_changed`: A thermostat's reported temperature changed by at least one degree Celsius.
* **Thermostat Temperature Reached Set Point** `thermostat.temperature_reached_set_point`: A thermostat's temperature reading is within one degree Celsius of the configured set point.
* **Thermostat Temperature Threshold Exceeded** `thermostat.temperature_threshold_exceeded`: A thermostat's temperature reading exceeded the set threshold.
* **Thermostat Temperature Threshold No Longer Exceeded** `thermostat.temperature_threshold_no_longer_exceeded`: A thermostat's temperature reading no longer exceeds the set threshold.
* **Unmanaged Access Code Converted To Managed** `access_code.unmanaged.converted_to_managed`: An unmanaged access code was converted successfully to a managed access code.
* **Unmanaged Access Code Created** `access_code.unmanaged.created`: An unmanaged access code was created on a device.
* **Unmanaged Access Code Failed To Convert To Managed** `access_code.unmanaged.failed_to_convert_to_managed`: An unmanaged access code failed to be converted to a managed access code.
* **Unmanaged Access Code Removed** `access_code.unmanaged.removed`: An unmanaged access code was removed from a device.
* **Unmanaged Device Connected** `device.unmanaged.connected`: The status of an unmanaged device changed from offline to online.
* **Unmanaged Device Converted To Managed** `device.unmanaged.converted_to_managed`: An unmanaged device was successfully converted to a managed device.
* **Unmanaged Device Disconnected** `device.unmanaged.disconnected`: The status of an unmanaged device changed from online to offline.

</details>
