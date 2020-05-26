# Base64 Encoding/Decoding

Useful shell scripts for fast base64 encoding and decoding.

## Usage

```
$ chmod a+x base64_encode.sh
$ chmod a+x base64_decode.sh

$ ./base64_encode Text to encode
$ ./base64_decode Text to decode
```

## Examples

```
$ ./base64_encode testing
$ ./base64_decode dGVzdGluZwo=
```

Or you can use them as a binary.

```
$ cp base64_encode /usr/bin/b64enc
$ cp base64_decode /usr/bin/b64dec

$ b64enc test
$ b64dec dGVzdGluZwo=
```
