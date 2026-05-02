# Binary Analysis Tools Reference

## Overview
Comprehensive tooling guide for reverse engineering and analyzing compiled binaries across all architectures.

## Tool Categories

### 1. Universal Binary Inspection
**Available on all systems:**
- `file` - Identify file type and architecture
- `strings` - Extract printable strings
- `hexdump` / `xxd` - Hex dump viewer
- `objdump` - Universal disassembler and object file viewer

### 2. ELF Analysis (Linux)
**Native Linux tools:**
- `readelf` - Display ELF file information
- `nm` - List symbols from object files
- `ldd` - Print shared library dependencies
- `size` - List section sizes
- `strip` - Remove symbols and debug info
- `patchelf` - Modify ELF binary properties

**Installation:**
```bash
sudo apt install binutils  # Ubuntu/Debian
```

### 3. Mach-O Analysis (macOS)
**Native macOS tools:**
- `otool` - Object file display tool
- `lipo` - Universal binary manipulation
- `nm` - Symbol listing
- `dyldinfo` - Dynamic linker information
- `codesign` - Code signature analysis

### 4. PE Analysis (Windows)
**Tools:**
- `objdump` (from binutils for Windows)
- `dumpbin` (Visual Studio)
- `PEview` (GUI tool)
- `CFF Explorer` (GUI tool)
- `pestudio` - Security analysis

### 5. Dynamic Analysis

#### System Call Tracing
**Linux:**
```bash
strace <binary>              # Trace system calls
strace -c <binary>           # Summary statistics
strace -e trace=open <binary> # Filter specific calls
strace -f <binary>           # Follow forks
```

**macOS:**
```bash
dtruss <binary>              # DTrace-based tracing
sudo dtruss -f <binary>      # Follow forks
```

**Cross-platform:**
- `ltrace` - Library call tracing (Linux)

#### Memory Analysis
```bash
# Memory leak detection
valgrind --leak-check=full <binary>

# Memory profiling
valgrind --tool=massif <binary>
heaptrack <binary>

# Memory mapping
pmap $(pgrep <process>)
cat /proc/<pid>/maps
```

#### Performance Profiling
**Linux:**
```bash
perf record <binary>         # Record performance data
perf report                  # Analyze recording
perf stat <binary>           # Statistics

# CPU profiling
perf record -g <binary>      # With call graph
```

**macOS:**
```bash
instruments -t "Time Profiler" <binary>
sample <process-name> 10     # Sample for 10 seconds
```

### 6. Disassemblers & Decompilers

#### Command-Line
**radare2** - Open source RE framework
```bash
r2 -A <binary>              # Auto-analyze
[0x00000000]> aaa           # Analyze all
[0x00000000]> afl           # List functions
[0x00000000]> pdf @ main    # Disassemble main
[0x00000000]> VV            # Visual graph mode
```

**objdump** - Universal disassembler
```bash
objdump -d <binary>                    # Disassemble
objdump -d -M intel <binary>           # Intel syntax
objdump -S <binary>                    # Source + asm (if available)
objdump -d --no-show-raw-insn <binary> # Cleaner output
```

#### GUI Tools
**Ghidra** (NSA, Free)
- Multi-architecture support
- Decompiler for C-like code
- Scripting with Python/Java
- Collaborative RE
- Installation: https://ghidra-sre.org/

**Binary Ninja** (Commercial, free tier)
- Modern UI
- High-level IL (HLIL)
- API for automation
- Multi-architecture
- Website: https://binary.ninja/

**IDA Pro / IDA Free**
- Industry standard
- Powerful scripting
- Large plugin ecosystem
- IDA Free: Limited features
- Website: https://hex-rays.com/

**Hopper** (macOS, Linux)
- Native macOS reverse engineering
- Clean interface
- ARM/x86/x64 support
- Website: https://www.hopperapp.com/

### 7. Security Analysis

#### Security Feature Detection
```bash
# checksec - Check security features
checksec --file=<binary>

# Manual checks
readelf -l <binary> | grep "GNU_STACK"    # NX bit
readelf -h <binary> | grep Type           # PIE
readelf -d <binary> | grep BIND_NOW       # RELRO
```

#### Vulnerability Scanning
```bash
# Scan for vulnerabilities
cwe_checker <binary>

# Find dangerous functions
objdump -d <binary> | grep -E "gets|strcpy|sprintf"
```

### 8. Architecture-Specific Tools

#### ARM/ARM64
```bash
# Emulation
qemu-arm-static <arm-binary>
qemu-aarch64-static <arm64-binary>

# Disassembly
arm-linux-gnueabi-objdump -d <arm-binary>
aarch64-linux-gnu-objdump -d <arm64-binary>
```

#### RISC-V
```bash
# Emulation
qemu-riscv64-static <riscv-binary>

# Disassembly
riscv64-linux-gnu-objdump -d <riscv-binary>
```

#### x86/x64
```bash
# Native tools work
objdump -d <binary>
gdb <binary>
```

### 9. Binary Diffing
**Tools for comparing binaries:**
- `bindiff` - Binary diffing plugin for IDA
- `diaphora` - Binary diffing for IDA and Ghidra
- `radiff2` - radare2 binary diffing
- `cmp` / `diff` - Simple byte comparison

```bash
# Simple byte diff
cmp <binary1> <binary2>

# Detailed diff
radiff2 <binary1> <binary2>

# Symbol diff
nm <binary1> > /tmp/symbols1
nm <binary2> > /tmp/symbols2
diff /tmp/symbols1 /tmp/symbols2
```

### 10. Network Analysis
**For analyzing network behavior:**
```bash
# Packet capture
tcpdump -i any -w capture.pcap
wireshark capture.pcap

# Network syscalls
strace -e trace=socket,connect,send,recv <binary>

# Active connections
netstat -tulpn | grep <process>
ss -tulpn | grep <process>
```

### 11. Debugging
**Interactive debuggers:**
- `gdb` - GNU Debugger (Linux, macOS, Windows)
- `lldb` - LLVM Debugger (macOS, Linux)
- `windbg` - Windows Debugger

```bash
# gdb basics
gdb <binary>
(gdb) break main
(gdb) run
(gdb) step
(gdb) print <var>
(gdb) disassemble
```

### 12. Specialized Tools

#### Binary Size Analysis
```bash
# Section sizes
size <binary>

# Detailed bloat analysis
bloaty <binary>              # Google's bloaty tool

# Symbol size
nm -S --size-sort <binary> | tail -20
```

#### Emulation
```bash
# QEMU user-mode (run binaries from other architectures)
qemu-arm-static <arm-binary>
qemu-riscv64-static <riscv-binary>

# Full system emulation
qemu-system-x86_64 -hda disk.img
```

## Tool Installation Guide

### Ubuntu/Debian
```bash
# Basic tools
sudo apt install binutils file strace ltrace

# Analysis tools
sudo apt install radare2 gdb valgrind

# Binary utilities
sudo apt install checksec qemu-user-static

# Optional: Install Ghidra
wget https://github.com/NationalSecurityAgency/ghidra/releases/download/...
unzip ghidra_*.zip
cd ghidra_*
./ghidraRun
```

### macOS
```bash
# Basic tools (built-in)
# file, otool, nm, lipo are pre-installed

# Additional tools via Homebrew
brew install binutils radare2 lldb

# Ghidra
brew install --cask ghidra
```

### Cross-compilation toolchains
```bash
# ARM toolchain
sudo apt install gcc-arm-linux-gnueabi gcc-aarch64-linux-gnu

# RISC-V toolchain
sudo apt install gcc-riscv64-linux-gnu
```

## Quick Reference Commands

### Identify binary
```bash
file <binary>
readelf -h <binary>  # ELF
otool -hv <binary>   # Mach-O
```

### Extract metadata
```bash
nm <binary>           # Symbols
ldd <binary>          # Dependencies
strings <binary>      # Strings
readelf -a <binary>   # All ELF info
```

### Disassemble
```bash
objdump -d <binary>             # All code
objdump -d -M intel <binary>    # Intel syntax
r2 -A <binary>                  # radare2 auto-analysis
```

### Dynamic analysis
```bash
strace <binary>                 # Syscalls
ltrace <binary>                 # Library calls
valgrind <binary>               # Memory check
perf stat <binary>              # Performance
```

### Security check
```bash
checksec --file=<binary>
nm <binary> | grep -E "gets|strcpy|sprintf"
```

## Best Practices

1. **Start with static analysis** before running unknown binaries
2. **Use sandboxing** (VM, container) for untrusted binaries
3. **Check security features** early to understand mitigations
4. **Combine tools** - each has strengths, no single tool is complete
5. **Take notes** - RE is iterative, document findings as you go
6. **Use version control** - track analysis state with Git
7. **Automate repetitive tasks** - script common analysis patterns
8. **Cross-reference** - compare disassembly with strings/syscalls for context

## Learning Resources

- **Practical Malware Analysis** - Classic RE book
- **Reverse Engineering for Beginners** - Free online book
- **Ghidra docs** - https://ghidra.re/
- **radare2 book** - https://book.rada.re/
- **Linux binary exploitation** - pwn.college, pwnable.kr
- **CTF challenges** - Great for practice (crackmes.one, root-me.org)
