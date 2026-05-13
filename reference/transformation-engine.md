---
description: >-
  Field Mapper syntax, built-in transform functions, and Type Coercer rules for
  data conversion between systems.
---

# Transformation Engine

The Transformation Engine handles data format conversion when data moves between connectors through the CDM. It has three components: Field Mapper, built-in transforms, and Type Coercer.

### Field Mapper

Maps fields between source and target systems using JSONPath-based dot notation with array index support.

#### Syntax

```
source.field.path → target.field.path
```

**Dot notation:** `order.customer.email` → `contact.email`

**Array access:** `order.lineItems[0].price` → `invoice.lines[0].unitPrice`

**Nested objects:** `order.shippingAddress.city` → `fulfillment.destination.city`

#### Mapping modes

| Mode                    | Description                                                      |
| ----------------------- | ---------------------------------------------------------------- |
| **Auto-mapping**        | Fields with matching names and types are mapped automatically    |
| **Manual mapping**      | User specifies source → target field pairs explicitly            |
| **AI-assisted mapping** | The Configuration Agent proposes mappings with confidence scores |

### Built-in transforms

Apply transformations during field mapping. Transforms can be chained.

#### String transforms

| Transform | Input             | Output          | Description                                |
| --------- | ----------------- | --------------- | ------------------------------------------ |
| `UPPER`   | `"hello world"`   | `"HELLO WORLD"` | Convert to uppercase                       |
| `LOWER`   | `"Hello World"`   | `"hello world"` | Convert to lowercase                       |
| `TRIM`    | `" hello "`       | `"hello"`       | Remove leading/trailing whitespace         |
| `CONCAT`  | `["John", "Doe"]` | `"John Doe"`    | Concatenate values with optional separator |

#### Numeric transforms

| Transform  | Input       | Output  | Description                                    |
| ---------- | ----------- | ------- | ---------------------------------------------- |
| `ROUND`    | `99.956`    | `99.96` | Round to specified decimal places (default: 2) |
| `MULTIPLY` | `(10, 1.1)` | `11`    | Multiply two values                            |
| `ADD`      | `(10, 5)`   | `15`    | Add two values                                 |

#### Utility transforms

| Transform  | Input                    | Output       | Description                            |
| ---------- | ------------------------ | ------------ | -------------------------------------- |
| `COALESCE` | `[null, "", "fallback"]` | `"fallback"` | Return first non-null, non-empty value |

### Type Coercer

Handles data type conversion between systems that represent the same data differently.

#### Date coercion

The Type Coercer auto-detects source date format and converts to the target format:

| Source format                 | Example                | Detection                                    |
| ----------------------------- | ---------------------- | -------------------------------------------- |
| Unix timestamp (seconds)      | `1704067200`           | Numeric, 10 digits                           |
| Unix timestamp (milliseconds) | `1704067200000`        | Numeric, 13 digits                           |
| ISO 8601                      | `2024-01-01T00:00:00Z` | String with T separator                      |
| MM-DD-YYYY                    | `01-01-2024`           | String, month-first pattern                  |
| DD-MM-YYYY                    | `01-01-2024`           | String, day-first pattern (locale-dependent) |

#### Number coercion

Locale-aware number parsing:

| Source        | Parsed value | Notes                                       |
| ------------- | ------------ | ------------------------------------------- |
| `"1,234.56"`  | `1234.56`    | US/UK format (comma as thousands separator) |
| `"1.234,56"`  | `1234.56`    | EU format (period as thousands separator)   |
| `"1234.56"`   | `1234.56`    | No thousands separator                      |
| `"$1,234.56"` | `1234.56`    | Currency symbol stripped                    |

#### Boolean coercion

| Source                            | Parsed value |
| --------------------------------- | ------------ |
| `"true"`, `"yes"`, `"1"`, `"on"`  | `true`       |
| `"false"`, `"no"`, `"0"`, `"off"` | `false`      |
| `1`                               | `true`       |
| `0`                               | `false`      |

#### Currency handling

Currency values are stored as **strings, not floats** to avoid floating-point precision issues.

| Source                | Stored as | Notes               |
| --------------------- | --------- | ------------------- |
| `99.99` (number)      | `"99.99"` | Converted to string |
| `"$99.99"` (string)   | `"99.99"` | Symbol stripped     |
| `"99,99"` (EU format) | `"99.99"` | Locale-normalized   |

#### Enum coercion

Maps between different enum representations:

```
Source: "PAID" → Target: "paid"
Source: "in_progress" → Target: "IN_PROGRESS"
Source: "1" → Target: "active"
```

Enum mappings are configured per field in the field mapping setup. Unmapped enum values flag an error in the execution log.

#### Auto-coerce function

The `autoCoerce` function detects the source type and applies the appropriate conversion automatically:

1. Detect source type (string, number, boolean, date)
2. Detect source format (ISO date, Unix timestamp, locale number, etc.)
3. Apply conversion to target type
4. Return converted value or throw with descriptive error
