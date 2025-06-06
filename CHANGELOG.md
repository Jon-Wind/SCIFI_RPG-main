# Changelog

## [Unreleased] - 2025-06-06

### Added
- Base `StationItem` class for game items with basic examination functionality
- `DiagnosticTool` class that inherits from `StationItem`
- `EnergyCrystal` class that inherits from `StationItem`
- `Player` class with inventory and location tracking
- `Location` class for managing game areas and their connections
- `GameController` class for managing game state and logic
- Basic movement and interaction system
- Player movement between locations
- Item interaction system (pick up tool, pick up crystal)
- Droid interaction using diagnostic tool
- Player status display

### Changed
- Improved `StationItem` class structure and inheritance
- Enhanced item examination functionality
- Updated game object initialization parameters
- Enhanced `Location.describe()` to show detailed room information
- Improved player movement feedback
- Streamlined item interaction messages

### Fixed
- Corrected class initialization parameters across all game objects
- Fixed method implementations in various classes
- Improved code organization and documentation
- Fixed droid presence state management
- Fixed item removal after pickup
