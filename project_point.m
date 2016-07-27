function p_img = project_point(p, f)
    %% TODO: Define and apply projection matrix
    m=[f 0 0 0; 0 f 0 0; 0 0 1 0];
    p=[p 1];
    p=p';
    p_proj=m*p;
    p_img=[p_proj(1)/p_proj(3) p_proj(2)/p_proj(3)];
end

