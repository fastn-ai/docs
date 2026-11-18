---
description: "Serverless Redis by Upstash."
hidden: true
---

# Upstash Redis

<img src="../../.gitbook/assets/connectors/lg/upstash-redis.png" alt="Upstash Redis logo">

Serverless Redis by Upstash. Run Redis commands over HTTP against your database's REST endpoint (strings, hashes, lists, sets, sorted sets, keys, pub/sub, pipelines and transactions), and manage your Upstash account's Redis databases (create, list, rename, delete, reset password, and view usage stats) via the Developer API.

| | |
| --- | --- |
| **Category** | [Data and databases](README.md) |
| **Website** | [upstash.com](https://upstash.com) |
| **Authentication** | Basic auth, Credentials you enter |
| **Slug** | `upstashRedis` |

## Use it

Add Upstash Redis from **Build → Integrations → Connectors** and connect an account, as in [Connect a system](../../build/connectors/connect-a-system.md). In workflow code, call an action as `fastn.connector.upstashRedis.<action>()`, with the action's slug from the table below. See [Workflow runtime API](../../reference/workflow-runtime.md).

## Actions

| Action | Slug | What it does |
| --- | --- | --- |
| Add Set Member | `addSetMember` | Adds a member to a set (SADD). Creates the set if it does not exist. Has no effect if the member is already present. |
| Add Sorted Set Member | `addSortedSetMember` | Adds a member with a score to a sorted set (ZADD), or updates its score if it already exists. Creates the sorted set if it does not exist. |
| Append To Value | `appendToValue` | Appends a string to the value already stored at a key. Creates the key with the given value if it does not exist. |
| Change Database Plan | `changeDatabasePlan` | Changes the pricing plan of an Upstash Redis database. Moving to a paid plan changes what the account is billed, so confirm the target plan before running this action. |
| Check Hash Field Exists | `checkHashFieldExists` | Checks whether a field exists in a hash (HEXISTS). |
| Check Key Exists | `checkKeyExists` | Checks whether a key exists (EXISTS), regardless of its data type. |
| Check Set Membership | `checkSetMembership` | Checks whether a value is a member of a set (SISMEMBER). |
| Create Database Backup | `createDatabaseBackup` | Takes an on-demand backup of an Upstash Redis database. Backups are a paid-plan feature. |
| Create Redis Database | `createRedisDatabase` | Creates a new Redis database in your Upstash account, via the Developer (Management) API. |
| Decrement Value | `decrementValue` | Decrements the integer value stored at a key by one. If the key does not exist, it is set to 0 before the decrement. |

<details>

<summary>See 71 more actions</summary>

* **Delete Database Backup** `deleteDatabaseBackup`: Deletes a single backup of an Upstash Redis database. The database itself is unaffected.
* **Delete Hash Field** `deleteHashField`: Removes a field from a hash (HDEL).
* **Delete JSON Value** `deleteJsonValue`: Deletes the JSON value at the given path within a JSON document key (JSON.DEL). Use path "$" to delete the whole document (removing the key). Requires a RedisJSON-capable database.
* **Delete Key** `deleteKey`: Deletes a key (DEL), regardless of its data type. Has no effect if the key does not exist.
* **Delete Redis Database** `deleteRedisDatabase`: Permanently deletes a Redis database from your Upstash account, via the Developer (Management) API. This cannot be undone.
* **Disable Daily Database Backup** `disableDailyDatabaseBackup`: Turns off the daily backup schedule for an Upstash Redis database. Existing backups are kept.
* **Disable Database Auto Upgrade** `disableDatabaseAutoUpgrade`: Disables Auto Upgrade on an Upstash Redis database, so it stays on its current plan when it exceeds its limits.
* **Disable Database Eviction** `disableDatabaseEviction`: Disables key eviction on an Upstash Redis database, so that writes fail once the database reaches its memory limit rather than evicting keys.
* **Enable Daily Database Backup** `enableDailyDatabaseBackup`: Turns on the daily backup schedule for an Upstash Redis database. Backups are a paid-plan feature.
* **Enable Database Auto Upgrade** `enableDatabaseAutoUpgrade`: Enables Auto Upgrade on an Upstash Redis database, allowing Upstash to move it to a larger plan automatically when it exceeds its current limits. This can increase the account's monthly cost.
* **Enable Database Eviction** `enableDatabaseEviction`: Enables key eviction on an Upstash Redis database, so that keys are evicted once the database reaches its memory limit instead of writes failing.
* **Enable Database TLS** `enableDatabaseTls`: Enables TLS encryption on an Upstash Redis database, via the Developer (Management) API.
* **Execute Pipeline** `executePipeline`: Runs a batch of Redis commands in a single HTTP call for lower latency (Upstash pipeline). Commands run in order but are NOT atomic - a failure in one command does not roll back the others. Provide a JSON array of commands, each itself a JSON array, e.g. [["SET","key1","value1"],["GET","key1"],["INCR","counter"]].
* **Execute Redis Command** `executeRedisCommand`: Runs any Redis command against the database over the REST API, for full coverage of commands not wrapped as their own action. Provide the full command as a JSON array with the command name first, e.g. ["ZADD","leaderboard","100","player1"] or ["EXPIRE","mykey","60"].
* **Execute Transaction** `executeTransaction`: Runs a batch of Redis commands atomically in a single HTTP call (Upstash multi-exec). Either all commands are applied or, if any command has a syntax error or is unsupported, the entire transaction is rejected. Provide a JSON array of commands, each itself a JSON array, e.g. [["SET","key1","value1"],["INCR","counter"]].
* **Find Keys By Pattern** `findKeysByPattern`: Returns all keys matching a glob-style pattern (KEYS). Scans the whole keyspace, so avoid using it on large databases in production; SCAN is the incremental alternative.
* **Get All Hash Fields** `getAllHashFields`: Returns all fields and values in a hash (HGETALL) as a flat array alternating field, value, field, value.
* **Get Hash Field** `getHashField`: Returns the value of a field in a hash (HGET). Returns null if the field or hash does not exist.
* **Get Hash Keys** `getHashKeys`: Returns all field names in a hash (HKEYS).
* **Get Hash Length** `getHashLength`: Returns the number of fields in a hash (HLEN).
* **Get Hash Values** `getHashValues`: Returns all values in a hash (HVALS), in the same order as the fields.
* **Get JSON Value** `getJsonValue`: Returns the JSON value at the root of a JSON document key (JSON.GET), serialized as a JSON string. Requires a RedisJSON-capable database.
* **Get JSON Value Type** `getJsonValueType`: Returns the JSON type (object, array, string, integer, number, boolean, or null) at the root of a JSON document key (JSON.TYPE). Requires a RedisJSON-capable database.
* **Get Key TTL** `getKeyTtl`: Returns the remaining time to live of a key in seconds (TTL). Returns -1 if the key has no expiry, or -2 if it does not exist.
* **Get Key Type** `getKeyType`: Returns the Redis data type stored at a key (TYPE) - e.g. string, list, set, zset, hash, or none if the key does not exist.
* **Get List Length** `getListLength`: Returns the number of elements in a list (LLEN).
* **Get List Range** `getListRange`: Returns a range of elements from a list (LRANGE), zero-based and inclusive. Use 0 and -1 to return the whole list.
* **Get Multiple Keys** `getMultipleKeys`: Retrieves the string values for several keys at once (MGET). Provide the full Redis command as a JSON array: the first element must be the literal string "MGET", followed by the keys to fetch, e.g. ["MGET","key1","key2","key3"].
* **Get Redis Database** `getRedisDatabase`: Returns the full configuration and connection details of a single Redis database in your Upstash account, via the Developer (Management) API.
* **Get Redis Database Stats** `getRedisDatabaseStats`: Returns usage and performance statistics for a Redis database - throughput, latency, storage, bandwidth, and monthly billing totals - via the Developer (Management) API.
* **Get Set Cardinality** `getSetCardinality`: Returns the number of members in a set (SCARD).
* **Get Set Members** `getSetMembers`: Returns all members of a set (SMEMBERS).
* **Get Sorted Set Cardinality** `getSortedSetCardinality`: Returns the number of members in a sorted set (ZCARD).
* **Get Sorted Set Range** `getSortedSetRange`: Returns a range of members from a sorted set (ZRANGE), ordered by ascending score. Zero-based and inclusive; use 0 and -1 to return all members.
* **Get Sorted Set Rank** `getSortedSetRank`: Returns the zero-based rank (ascending score order) of a member in a sorted set (ZRANK). Returns null if the member does not exist.
* **Get Sorted Set Score** `getSortedSetScore`: Returns the score of a member in a sorted set (ZSCORE). Returns null if the member does not exist.
* **Get String Length** `getStringLength`: Returns the length of the string value stored at a key. Returns 0 if the key does not exist.
* **Get Substring** `getSubstring`: Returns the substring of the string value stored at a key, between the given start and end offsets (GETRANGE, zero-based, inclusive; negative offsets count from the end).
* **Get Value** `getValue`: Retrieves the string value stored at the given key. Returns null in the result if the key does not exist.
* **Increment Hash Field** `incrementHashField`: Increments the integer value of a hash field by the given amount (HINCRBY). Creates the field with value 0 first if it does not exist.
* **Increment Sorted Set Score** `incrementSortedSetScore`: Increments the score of a member in a sorted set by the given amount (ZINCRBY). Adds the member with that score if it does not exist.
* **Increment Value** `incrementValue`: Increments the integer value stored at a key by one. If the key does not exist, it is set to 0 before the increment.
* **Intersect Sets** `intersectSets`: Returns the intersection of two sets (SINTER) - members present in both sets.
* **List Database Backups** `listDatabaseBackups`: Lists every backup taken of an Upstash Redis database, with each backup's size, state and creation time.
* **List Redis Databases** `listRedisDatabases`: Lists every Redis database in your Upstash account, via the Developer (Management) API.
* **List Teams** `listTeams`: Lists every Upstash team the account belongs to. Use the returned team ID with Move Database To Team.
* **Move Database To Team** `moveDatabaseToTeam`: Moves an Upstash Redis database from the personal account into a team, transferring ownership and billing to that team.
* **Pop Left** `popLeft`: Removes and returns the first element (head) of a list (LPOP). Returns null if the list is empty or does not exist.
* **Pop Right** `popRight`: Removes and returns the last element (tail) of a list (RPOP). Returns null if the list is empty or does not exist.
* **Publish Message** `publishMessage`: Publishes a message to a Redis Pub/Sub channel (PUBLISH). Note: Redis SUBSCRIBE itself is not exposed as an action - it is a long-lived streaming operation (available from Upstash only via Server-Sent Events) that does not fit this connector's request/response action model.
* **Push Left** `pushLeft`: Inserts a value at the head (left) of a list (LPUSH). Creates the list if it does not exist.
* **Push Right** `pushRight`: Inserts a value at the tail (right) of a list (RPUSH). Creates the list if it does not exist.
* **Remove Key Expiry** `removeKeyExpiry`: Removes the expiry from a key, making it persist forever (PERSIST).
* **Remove List Elements** `removeListElements`: Removes elements equal to the given value from a list (LREM). A positive count removes from the head, a negative count removes from the tail, and 0 removes all occurrences.
* **Remove Set Member** `removeSetMember`: Removes a member from a set (SREM).
* **Remove Sorted Set Member** `removeSortedSetMember`: Removes a member from a sorted set (ZREM).
* **Rename Key** `renameKey`: Renames a key (RENAME). Overwrites the destination key if it already exists. Fails if the source key does not exist.
* **Rename Redis Database** `renameRedisDatabase`: Renames an existing Redis database in your Upstash account, via the Developer (Management) API.
* **Reset Redis Database Password** `resetRedisDatabasePassword`: Resets the password (and REST token) of a Redis database, via the Developer (Management) API. Any application using the old REST token or connection password must be updated afterward.
* **Restore Database Backup** `restoreDatabaseBackup`: Restores an Upstash Redis database from an existing backup. This overwrites the database's current contents with the backup's data.
* **Scan Keys** `scanKeys`: Incrementally iterates the keyspace (SCAN) without blocking the database. Start with cursor 0 and keep calling with the returned cursor until it comes back as 0.
* **Set Hash Field** `setHashField`: Sets the value of a field in a hash (HSET). Creates the hash if it does not exist.
* **Set JSON Value** `setJsonValue`: Sets a JSON value at the given path within a JSON document key (JSON.SET). Use path "$" for the document root. Creates the key if it does not exist. Requires a RedisJSON-capable database.
* **Set Key Expiry** `setKeyExpiry`: Sets a key to expire after the given number of seconds (EXPIRE).
* **Set Multiple Keys** `setMultipleKeys`: Sets several string keys at once (MSET), overwriting any existing values. Provide the full Redis command as a JSON array: the first element must be the literal string "MSET", followed by alternating key and value strings, e.g. ["MSET","key1","value1","key2","value2"].
* **Set Substring** `setSubstring`: Overwrites part of the string value stored at a key, starting at the given offset (SETRANGE). Pads with zero bytes if the offset is beyond the current length.
* **Set Value** `setValue`: Sets a string value for the given key, optionally with an expiry or existence condition. Overwrites any existing value.
* **Set Value With Expiry** `setValueWithExpiry`: Sets a string value for the given key and makes it expire after the specified number of seconds (SETEX).
* **Union Sets** `unionSets`: Returns the union of two sets (SUNION) - all members present in either set, with duplicates removed.
* **Update Database Budget** `updateDatabaseBudget`: Updates the monthly spending budget of an Upstash Redis database, in US dollars.
* **Update Database Regions** `updateDatabaseRegions`: Replaces the set of read regions on a global Upstash Redis database. The supplied list becomes the complete set of read replicas, so include every region the database should keep.

</details>
