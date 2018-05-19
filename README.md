# obs-service-rust2rpm

OBS Source Service to auto-generate packages for Rust crates

## Requirements

* [`rust2rpm`](https://pagure.io/fedora-rust/rust2rpm) v6 or newer

## How to use

To use this source service, add a snippet to `_service` like the following in the `services` block:

```xml
  <service name="rust2rpm">
    <param name="name">libc</param>
    <param name="type">fedora</param>
  </service>
```

The full schema is described in the `obs-rust2rpm.service` file in this repository.
