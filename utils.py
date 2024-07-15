import numpy as np
from typing import Literal, Optional

# constants of shame
EARTH_RADIUS_KM = 6371
DAY_PER_YEAR = 365
SEC_PER_DAY = 86400


def get_xyz_from_lonlat(
    lon: np.ndarray, lat: np.ndarray, depth_km: Optional[np.ndarray] = None
) -> np.ndarray:
    """Converts longitude, latitude, and depth to x, y, and z Cartesian
    coordinates.

    Args:
        lon: The longitude, in degrees.
        lat: The latitude, in degrees.
        depth_km: The depth, in kilometers.

    Returns:
        The Cartesian coordinates (x, y, z), in kilometers.
    """
    # Check the shapes of the input arrays
    if lon.shape != lat.shape:
        raise ValueError("lon and lat must have the same shape")

    assert -180 <= lon.all() <= 180, "Longitude must be between -180 and 180"
    assert -90 <= lat.all() <= 90, "Latitude must be between -90 and 90"
    assert depth_km is None or depth_km.all() >= 0, "Depth must be positive"

    # Assign zero depth if not provided:
    if depth_km is None:
        depth_km = np.zeros_like(lat)

    # Convert to radians
    lat_rad = lat * np.pi / 180
    lon_rad = lon * np.pi / 180

    # Calculate the distance from the center of the earth using the depth
    # and the radius of the earth (6371 km)
    r = EARTH_RADIUS_KM - depth_km

    # Calculate the x, y, z coordinates
    x = r * np.cos(lat_rad) * np.cos(lon_rad)
    y = r * np.cos(lat_rad) * np.sin(lon_rad)
    z = r * np.sin(lat_rad)

    return np.array([x, y, z]).T


class Scaling:
    """A collection of scaling relationships for earthquakes"""

    @staticmethod
    def magnitude_to_size(
        MW: np.ndarray, stress_drop_Pa=3e6, out_unit: Literal["km", "m"] = "km"
    ) -> np.ndarray:
        # M0 = mu * A * D ~ \delta \sigma * a^3                   # add constant?
        # Mw = (2/3) * (log10(M0) - 9.1)                    
        # a ~ [(1/(\delta \sigma)) 10^((3/2 * Mw) + 9.1)]^(1/3)   # TODO: CHECK THIS! e.g. dyne cm vs Pa
        # for SSEs \delta \sigma ~ 10 kPa
        # for Earthquake \delta \sigma ~ 3 MPa (default)
        # returns the dimensions of the earthquake in km

        unit_conversion_factor = {"km": 1 / 1000, "m": 1}

        return (10 ** ((3 / 2) * MW + 9.1) / stress_drop_Pa) ** (
            1 / 3
        ) * unit_conversion_factor[out_unit]
